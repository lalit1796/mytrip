# Generated by Django 2.2.2 on 2019-08-29 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0011_auto_20190827_2322'),
    ]

    operations = [
        migrations.RenameField(
            model_name='package',
            old_name='costingprize',
            new_name='costingprize_per_adult',
        ),
        migrations.RenameField(
            model_name='package',
            old_name='generalprize',
            new_name='generalprize_per_adult',
        ),
    ]
