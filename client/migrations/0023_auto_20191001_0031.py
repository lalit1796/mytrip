# Generated by Django 2.2.2 on 2019-09-30 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0022_auto_20190926_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_type',
            field=models.CharField(default='undefined', help_text='Payment Type', max_length=200),
        ),
    ]
