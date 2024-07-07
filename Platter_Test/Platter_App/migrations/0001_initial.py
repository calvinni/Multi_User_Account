# Generated by Django 4.1.3 on 2024-07-07 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Head_Office',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=255)),
                ('Password', models.CharField(max_length=255)),
                ('AccessLv', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='District_Office',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=255)),
                ('Password', models.CharField(max_length=255)),
                ('AccessLv', models.IntegerField(max_length=10)),
                ('HO_id', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='Platter_App.head_office')),
            ],
        ),
        migrations.CreateModel(
            name='Branch_Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=255)),
                ('Password', models.CharField(max_length=255)),
                ('AccessLv', models.IntegerField(max_length=10)),
                ('BL_id', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='Platter_App.district_office')),
            ],
        ),
    ]
