# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-13 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_projectimage_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectimage',
            options={'ordering': ('order',)},
        ),
        migrations.RenameField(
            model_name='project',
            old_name='type',
            new_name='project_type',
        ),
        migrations.AddField(
            model_name='projectimage',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
