# Generated by Django 2.2.2 on 2019-09-28 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0047_auto_20190929_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitysale',
            name='duration',
            field=models.CharField(default='0 hours', help_text='Mention Clear Durataion in minutes or hours or days. Eg: 15 minutes', max_length=200),
        ),
    ]
