# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 17:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('label', '0003_flaudb_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flaudb',
            name='test',
        ),
    ]
