# Generated by Django 3.0 on 2021-04-10 12:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_auto_20210410_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='createdOn',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 10, 18, 15, 27, 279753)),
        ),
    ]
