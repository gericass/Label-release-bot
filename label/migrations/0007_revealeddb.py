# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 05:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('label', '0006_owsladb'),
    ]

    operations = [
        migrations.CreateModel(
            name='revealeddb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=500, verbose_name='アーティスト名')),
            ],
        ),
    ]