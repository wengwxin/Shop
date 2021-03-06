# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-11-19 17:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='auction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auctionid', models.CharField(max_length=20)),
                ('auctionname', models.CharField(max_length=50)),
                ('auctionprice', models.DecimalField(decimal_places=2, max_digits=9)),
                ('auctionnum', models.CharField(max_length=20, null=True)),
                ('auctiondesc', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
