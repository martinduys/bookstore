# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20151214_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2015, 12, 15, 11, 26, 55, 392223, tzinfo=utc)),
        ),
    ]
