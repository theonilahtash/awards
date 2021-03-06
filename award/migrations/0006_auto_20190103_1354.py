# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-01-03 10:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('award', '0005_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='reviews',
            new_name='review',
        ),
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='review',
            name='design',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='review',
            name='usability',
            field=models.IntegerField(default=0),
        ),
    ]
