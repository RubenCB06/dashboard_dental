# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-10 19:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0002_auto_20160910_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='apellido_materno',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='apellido_paterno',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='correo',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='nom_paciente',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
