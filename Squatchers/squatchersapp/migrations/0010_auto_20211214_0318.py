# Generated by Django 3.2.8 on 2021-12-14 03:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squatchersapp', '0009_alter_sighting_sight_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sighting',
            name='sight_date',
            field=models.DateField(default=datetime.datetime(2021, 12, 14, 3, 18, 7, 902676)),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='sight_time',
            field=models.TimeField(default=datetime.datetime(2021, 12, 14, 3, 18, 7, 902720)),
        ),
    ]