# Generated by Django 3.0.4 on 2020-05-25 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0009_bike_batterie'),
    ]

    operations = [
        migrations.AddField(
            model_name='bike',
            name='eclairage',
            field=models.TextField(blank=True, null=True),
        ),
    ]