# Generated by Django 2.2.2 on 2019-09-23 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0031_auto_20190923_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitysale',
            name='uuid',
            field=models.CharField(default='7f3029ab', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='activitysale',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
