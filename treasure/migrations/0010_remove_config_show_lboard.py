# Generated by Django 2.1.4 on 2020-02-08 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('treasure', '0009_config_show_lboard'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='config',
            name='show_lboard',
        ),
    ]
