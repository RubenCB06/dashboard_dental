# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-04 14:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0002_auto_20160904_1434'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('time', models.TimeField()),
                ('issue', models.TextField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='docotor', to='consultas.Medico')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paciente', to='consultas.Paciente')),
            ],
        ),
    ]
