# Generated by Django 3.0 on 2021-04-25 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0015_auto_20210415_1818'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='language',
            new_name='languageSC',
        ),
        migrations.AlterField(
            model_name='authtoken',
            name='key',
            field=models.CharField(default='521481a5cded30dd110dbc408816113678cbaee1', max_length=40, primary_key=True, serialize=False, verbose_name='Key'),
        ),
    ]
