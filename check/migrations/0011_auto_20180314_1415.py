# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-14 05:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0010_group_unitlimit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='unitlimit',
            new_name='limit',
        ),
    ]