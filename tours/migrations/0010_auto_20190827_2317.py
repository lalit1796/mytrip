# Generated by Django 2.2.2 on 2019-08-27 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0009_package_dates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='mention_cities',
            field=models.CharField(help_text='Use same names of cities in citylist. eg: new delhi, chandigarh, manali, ...', max_length=255),
        ),
    ]
