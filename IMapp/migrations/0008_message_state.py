# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-06 12:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IMapp', '0007_remove_message_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='state',
            field=models.BooleanField(default=False),
        ),
    ]
