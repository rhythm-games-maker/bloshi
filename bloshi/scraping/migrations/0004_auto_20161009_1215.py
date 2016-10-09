# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-09 12:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0003_temporaryitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spider',
            name='shop_code',
            field=models.TextField(blank=True, verbose_name='shop_code'),
        ),
        migrations.AlterField(
            model_name='spider',
            name='shop_code_in',
            field=models.TextField(blank=True, verbose_name='shop_code input'),
        ),
        migrations.AlterField(
            model_name='spider',
            name='shop_code_out',
            field=models.TextField(blank=True, verbose_name='shop_code output'),
        ),
        migrations.AlterField(
            model_name='spider',
            name='shop_price',
            field=models.TextField(blank=True, verbose_name='shop_price'),
        ),
        migrations.AlterField(
            model_name='spider',
            name='shop_price_in',
            field=models.TextField(blank=True, verbose_name='shop_price input'),
        ),
        migrations.AlterField(
            model_name='spider',
            name='shop_price_out',
            field=models.TextField(blank=True, verbose_name='shop_price output'),
        ),
        migrations.AlterField(
            model_name='spider',
            name='shop_url',
            field=models.TextField(blank=True, verbose_name='shop_url'),
        ),
        migrations.AlterField(
            model_name='spider',
            name='shop_url_in',
            field=models.TextField(blank=True, verbose_name='shop_url input'),
        ),
        migrations.AlterField(
            model_name='spider',
            name='shop_url_out',
            field=models.TextField(blank=True, verbose_name='shop_url output'),
        ),
    ]
