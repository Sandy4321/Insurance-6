# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0003_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('sku', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('basePrice', models.CharField(max_length=200)),
                ('sellingPrice', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TextMessage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('mobileNo', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(default=datetime.datetime(2015, 11, 30, 13, 44, 40, 289021, tzinfo=utc), max_length=500),
            preserve_default=False,
        ),
    ]
