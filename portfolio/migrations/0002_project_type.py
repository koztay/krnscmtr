# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='type',
            field=models.CharField(choices=[('videowall', 'Videowall'), ('cctv', 'CCTV'), ('signage', 'Digital-Signage')], default='Videowall', max_length=50),
        ),
    ]
