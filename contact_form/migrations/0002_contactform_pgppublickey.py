# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-20 02:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_form', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='pgpPublicKey',
            field=models.TextField(default=''),
        ),
    ]
