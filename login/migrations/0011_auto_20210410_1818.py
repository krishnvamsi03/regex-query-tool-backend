# Generated by Django 3.0 on 2021-04-10 12:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_auto_20210410_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='createdOn',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
