# Generated by Django 3.2.8 on 2021-12-13 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squatchersapp', '0002_alter_sighting_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='sighting',
            name='sight_title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
