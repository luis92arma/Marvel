# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-22 18:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_cometario'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cometario',
            new_name='Comentario',
        ),
    ]