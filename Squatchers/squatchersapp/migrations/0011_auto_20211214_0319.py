# Generated by Django 3.2.8 on 2021-12-14 03:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squatchersapp', '0010_auto_20211214_0318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sighting',
            name='sight_date',
            field=models.DateField(default=datetime.datetime(2021, 12, 14, 3, 19, 29, 314346)),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='sight_time',
            field=models.TimeField(default=datetime.datetime(2021, 12, 14, 3, 19, 29, 314372)),
        ),
    ]
