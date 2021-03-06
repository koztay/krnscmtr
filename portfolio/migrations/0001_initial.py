# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-13 15:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioShortIntro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intro_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('type', models.CharField(choices=[('videowall', 'Videowall'), ('cctv', 'CCTV'), ('signage', 'Digital-Signage'), ('global', 'LG-Global')], default='Videowall', max_length=50)),
                ('finished_date', models.DateField(blank=True, null=True)),
                ('video_url', models.URLField(blank=True, null=True)),
            ],
            options={
                'ordering': ('-finished_date', 'title'),
            },
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='portfolio.Project')),
            ],
        ),
    ]
