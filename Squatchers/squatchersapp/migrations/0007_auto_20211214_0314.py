# Generated by Django 3.2.8 on 2021-12-14 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squatchersapp', '0006_auto_20211214_0254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sighting',
            name='Time_date',
        ),
        migrations.AddField(
            model_name='sighting',
            name='sight_date',
            field=models.DateField(default='2021-01-01'),
        ),
        migrations.AddField(
            model_name='sighting',
            name='sight_time',
            field=models.TimeField(default='03:14'),
        ),
    ]
