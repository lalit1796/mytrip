# Generated by Django 2.2.2 on 2019-09-26 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0042_auto_20190926_0109'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitysale',
            name='gst',
            field=models.IntegerField(default=5),
        ),
    ]
