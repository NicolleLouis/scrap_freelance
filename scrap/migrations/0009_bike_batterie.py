# Generated by Django 3.0.4 on 2020-05-25 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0008_bike_console'),
    ]

    operations = [
        migrations.AddField(
            model_name='bike',
            name='batterie',
            field=models.TextField(blank=True, null=True),
        ),
    ]
