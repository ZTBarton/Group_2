# Generated by Django 3.2.8 on 2021-12-14 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squatchersapp', '0018_alter_sighting_sight_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sighting',
            name='sight_datetime',
            field=models.DateTimeField(default='2000-01-01'),
        ),
    ]
