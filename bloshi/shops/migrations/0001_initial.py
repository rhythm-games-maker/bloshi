# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-08 13:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_code', models.CharField(blank=True, max_length=20, verbose_name='Shop code')),
                ('shop_title', models.CharField(blank=True, max_length=255, verbose_name='Shop title')),
                ('search_title', models.CharField(blank=True, max_length=255, verbose_name='Search title')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Title')),
                ('shop_url', models.URLField(blank=True, verbose_name='Shop URL')),
                ('shop_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Shop price')),
                ('is_listed', models.BooleanField(default=False, verbose_name='Is listed?')),
                ('is_followed', models.BooleanField(default=False, verbose_name='Is followed?')),
            ],
            options={
                'db_table': 'articles',
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('code', models.IntegerField(verbose_name='Code')),
            ],
            options={
                'db_table': 'availabilities',
                'verbose_name': 'Availability',
                'verbose_name_plural': 'Availabilities',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Name')),
                ('code', models.CharField(max_length=7, unique=True, verbose_name='Code')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='shops.Category')),
            ],
            options={
                'db_table': 'categories',
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='Name')),
                ('code', models.CharField(blank=True, max_length=3, verbose_name='Code')),
                ('url', models.URLField(blank=True, verbose_name='URL')),
            ],
            options={
                'db_table': 'shops',
                'verbose_name': 'Shop',
                'verbose_name_plural': 'Shops',
            },
        ),
        migrations.CreateModel(
            name='ShopAvailability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(blank=True, max_length=50, verbose_name='Keyword')),
                ('availability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shops.Availability')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shops.Shop')),
            ],
            options={
                'db_table': 'shopavailabilities',
                'verbose_name': 'Shop availability',
                'verbose_name_plural': 'Shop availabilities',
            },
        ),
        migrations.CreateModel(
            name='ShopCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='Name')),
                ('url', models.URLField(blank=True, verbose_name='URL')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shops.Category')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='shops.ShopCategory')),
                ('shop', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shops.Shop')),
            ],
            options={
                'db_table': 'shopcategories',
                'verbose_name': 'Shop category',
                'verbose_name_plural': 'Shop categories',
            },
        ),
        migrations.AddField(
            model_name='shop',
            name='availabilities',
            field=models.ManyToManyField(through='shops.ShopAvailability', to='shops.Availability'),
        ),
        migrations.AddField(
            model_name='shop',
            name='categories',
            field=models.ManyToManyField(through='shops.ShopCategory', to='shops.Category'),
        ),
        migrations.AddField(
            model_name='article',
            name='shop_availability',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shops.ShopAvailability'),
        ),
        migrations.AddField(
            model_name='article',
            name='shop_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shops.ShopCategory'),
        ),
    ]
