# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0002_auto_20170531_1119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='items',
        ),
        migrations.AddField(
            model_name='item',
            name='wishlist',
            field=models.ManyToManyField(to='wishlist.WishList'),
        ),
    ]
