# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-19 22:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='MEDIA_ROOT'),
        ),
    ]
