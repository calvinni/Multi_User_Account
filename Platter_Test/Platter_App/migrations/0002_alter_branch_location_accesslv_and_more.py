# Generated by Django 4.1.3 on 2024-07-07 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Platter_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch_location',
            name='AccessLv',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='district_office',
            name='AccessLv',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='head_office',
            name='AccessLv',
            field=models.CharField(max_length=255),
        ),
    ]
