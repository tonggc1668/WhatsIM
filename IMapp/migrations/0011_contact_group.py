# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-15 15:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IMapp', '0010_auto_20160511_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='group',
            field=models.CharField(default='DefaultGroup', max_length=20),
        ),
    ]
