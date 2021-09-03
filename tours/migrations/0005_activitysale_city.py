# Generated by Django 2.2.2 on 2019-08-14 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiling', '0002_auto_20190814_2235'),
        ('tours', '0004_auto_20190814_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitysale',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='city', to='profiling.City'),
            preserve_default=False,
        ),
    ]
