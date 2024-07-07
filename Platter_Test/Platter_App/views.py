from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.core.paginator import Paginator
from django.conf import settings
from rest_framework import viewsets
from itertools import chain

from Platter_App.models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def Login(request):
    return render(request, 'login.html')

def check_login(request):
    if request.method == "POST":
        AL = request.POST['accesslv']
        U = request.POST['username']
        P = request.POST['password']
        
        if AL == "Admin":
            user = Head_Office.objects.filter(Username=U).count()
        elif AL == "District":
            user = District_Office.objects.filter(Username=U).count()
        elif AL == "Branch":
            user = Branch_Location.objects.filter(Username=U).count()
        if user == 1:
            if AL == "Admin":
                member = Head_Office.objects.get(Username=U)
            elif AL == "District":
                member = District_Office.objects.get(Username=U)
            elif AL == "Branch":
                member = Branch_Location.objects.get(Username=U)
            #checkP = check_password(P, member.password)
            if member.Password == P:
                request.session['member_id'] = member.id
                request.session['member_name'] = member.Username
                request.session['Access'] = member.AccessLv
                messages.success(request, f"Successfully logged in")
                return HttpResponseRedirect(reverse('index'))
            else:
                messages.error(request, P)
                return HttpResponseRedirect(reverse('login'))
        else:
            messages.error(request, 'There are no users with that name')
            return HttpResponseRedirect(reverse('login'))
    else:
        messages.error(request, 'Do not access this url directly')
        return HttpResponseRedirect(reverse('login'))
    
def Logout(request):
    if 'member_id' in request.session: #Check if user is logged in
        try:
            del request.session['member_id']
            request.session.clear_expired()
            return HttpResponseRedirect(reverse('index'))
        except KeyError:
            messages.error(request, 'Something went wrong try again')
            return HttpResponseRedirect(reverse('index'))
    else:
        messages.error(request, 'session timed out, Please login')
        return HttpResponseRedirect(reverse('index'))

def List(request):
    if 'member_id' in request.session: #Check if user is logged in
        session_id = request.session['member_id']
        session_access = request.session['Access']
        if session_access == "Admin":
            HOdata = Head_Office.objects.filter(id=session_id).select_related()
            DOdata = District_Office.objects.filter(HO_id_id=session_id).select_related()
            BLdata = Branch_Location.objects.filter(DO_id_id=session_id).select_related()
            postdata = list(chain(HOdata, DOdata, BLdata))
        elif session_access == "District":
            DOdata = District_Office.objects.filter(HO_id_id=session_id).select_related()
            BLdata = Branch_Location.objects.filter(DO_id_id=session_id).select_related()
            postdata = list(chain(DOdata, BLdata))
        
        paginator = Paginator(postdata, 3)
        page_number = request.GET.get('page')
        page_posts = paginator.get_page(page_number)
        
        template = loader.get_template('list.html')
        context = {
            'page_posts': page_posts,
        }
        return HttpResponse(template.render(context, request))
    else:
        messages.error(request, 'session timed out, Please login')
        return HttpResponseRedirect(reverse('index'))

def Register(request):
    return render(request, 'register.html')

def CreateAcc(request):
    if request.method == "POST":
        if 'member_id' in request.session: #Check if user is logged in
            session_id = request.session['member_id']
            AL = request.POST['accesslv']
            U = request.POST['username']
            P = request.POST['password']
            if AL == "District":
                insertData = District_Office(
                                            Username=U, 
                                            Password=P, 
                                            AccessLv=AL, 
                                            HO_id_id=session_id)
                insertData.save()
            elif AL == "Branch":
                insertData = Branch_Location(
                                            Username=U, 
                                            Password=P, 
                                            AccessLv=AL,
                                            DO_id_id=session_id)
                insertData.save()
            messages.success(request, 'Account have been created')
            return HttpResponseRedirect(reverse('list'))
        else:
            messages.error(request, 'session timed out, Please login')
            return HttpResponseRedirect(reverse('index'))
    else:
        messages.error(request, 'Do not access these url directly')
        return HttpResponseRedirect(reverse('index'))