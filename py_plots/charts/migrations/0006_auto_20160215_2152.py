# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-15 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0005_auto_20160215_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plotimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
