# Generated by Django 2.2.2 on 2019-09-23 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0032_auto_20190923_2123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activitysale',
            name='uuid',
        ),
    ]
