# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-19 14:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-creado',)},
        ),
        migrations.RemoveField(
            model_name='post',
            name='fecha',
        ),
        migrations.AddField(
            model_name='post',
            name='actualizado',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='creado',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique_for_date='creado'),
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(blank=True, choices=[('draft', 'Draft'), ('piblished', 'Published')], default='draft', max_length=10, null=True),
        ),
    ]
