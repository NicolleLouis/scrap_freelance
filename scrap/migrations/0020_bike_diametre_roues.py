# Generated by Django 3.0.4 on 2020-05-28 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0019_bike_suspension'),
    ]

    operations = [
        migrations.AddField(
            model_name='bike',
            name='diametre_roues',
            field=models.TextField(blank=True, null=True),
        ),
    ]
