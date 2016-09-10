# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-10 18:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_medico_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='especialidad',
            field=models.CharField(choices=[('Endodoncia', 'Endodoncia'), ('Odontopediatría', 'Odontopediatría'), ('Ortodoncia', 'Ortodoncia'), ('Periodoncia', 'Periodoncia'), ('Implantología', 'Implantología'), ('Prótesis Bucal', 'Prótesis Bucal'), ('Prótesis Maxilofacial', 'Prótesis Maxilofacial'), ('Salud Pública Bucal', 'Salud Pública Bucal'), ('Materiales Dentales', 'Materiales Dentales'), ('Patologia Bucal', 'Patologia Bucal')], default='Ortodoncia', max_length=140),
        ),
    ]
