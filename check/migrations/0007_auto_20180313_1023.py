# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-13 01:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0006_auto_20180313_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='attend',
            field=models.CharField(choices=[('LA', '지각'), ('EA', '조퇴'), ('AB', '결석'), ('OU', '외출')], max_length=2),
        ),
    ]
