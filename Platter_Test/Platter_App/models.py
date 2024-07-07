from django.db import models


###########################################################################################################################
# Create your models here.
#Query tables

# No Primary ID as SQLlite will create a basic auto-incrementing ID when building it.
class Head_Office(models.Model):
    Username = models.CharField(max_length=255, unique=True)
    Password = models.CharField(max_length=255)
    AccessLv = models.CharField(max_length=255)
    
    def __str__(self):
        return self.id
    
class District_Office(models.Model):
    HO_id = models.ForeignKey(Head_Office, 
                              on_delete=models.CASCADE, 
                              db_constraint=False)
    Username = models.CharField(max_length=255, unique=True)
    Password = models.CharField(max_length=255)
    AccessLv = models.CharField(max_length=255)
    
    def __str__(self):
        return self.id

class Branch_Location(models.Model):
    DO_id = models.ForeignKey(District_Office,
                              on_delete=models.CASCADE, 
                              db_constraint=False)
    Username = models.CharField(max_length=255, unique=True)
    Password = models.CharField(max_length=255)
    AccessLv = models.CharField(max_length=255)
    
    def __str__(self):
        return self.id