# Generated by Django 3.0.4 on 2020-05-28 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0013_bike_consolle'),
    ]

    operations = [
        migrations.AddField(
            model_name='bike',
            name='gamme',
            field=models.TextField(blank=True, null=True),
        ),
    ]
