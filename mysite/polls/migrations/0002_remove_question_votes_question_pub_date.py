# Generated by Django 4.2.5 on 2023-12-11 09:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='votes',
        ),
        migrations.AddField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 11, 9, 10, 57, 629777, tzinfo=datetime.timezone.utc), verbose_name='date published'),
            preserve_default=False,
        ),
    ]
