# Generated by Django 4.2.1 on 2023-05-28 12:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Graph',
        ),
        migrations.AddField(
            model_name='deviceinformation',
            name='percentage',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='deviceinformation',
            name='timestamp',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='deviceinformation',
            name='update_at',
            field=models.DateField(auto_now=True),
        ),
    ]