# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-10 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medico',
            name='apellido_materno',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='medico',
            name='apellido_paterno',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='medico',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='medico',
            name='nombre',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
