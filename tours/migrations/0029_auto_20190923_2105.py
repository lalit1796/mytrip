# Generated by Django 2.2.2 on 2019-09-23 15:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0028_auto_20190922_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitysale',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
