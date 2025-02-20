# Generated by Django 5.0.8 on 2024-09-10 13:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('description', models.CharField(blank=True)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('creation_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
