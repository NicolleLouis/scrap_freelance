# Generated by Django 3.0.4 on 2020-05-20 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0002_bike'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bike',
            name='is_finished',
        ),
    ]
