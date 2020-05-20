# Generated by Django 3.0.4 on 2020-05-20 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_scrapped', models.BooleanField(default=False)),
                ('page_url', models.TextField(blank=True, null=True)),
                ('picture_url', models.TextField(blank=True, null=True)),
                ('brand', models.TextField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('category', models.TextField(blank=True, null=True)),
                ('is_finished', models.BooleanField(default=False)),
            ],
        ),
    ]