# Generated by Django 2.2.2 on 2019-08-31 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0018_remove_package_costingprize_per_child'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='discount_max',
            field=models.IntegerField(default=0, help_text='Discount applicable for 2 individual.'),
        ),
        migrations.AddField(
            model_name='package',
            name='discount_pax6',
            field=models.IntegerField(default=0, help_text='Discount applicable for 2 individual.'),
        ),
        migrations.AddField(
            model_name='package',
            name='discount_pax8',
            field=models.IntegerField(default=0, help_text='Discount applicable for 2 individual.'),
        ),
        migrations.AlterField(
            model_name='package',
            name='discount_pax2',
            field=models.IntegerField(default=0, help_text='Discount applicable for 2 individual.(1 adult + 1 child) or 2 adults; on their rspective charges.'),
        ),
        migrations.AlterField(
            model_name='package',
            name='discount_pax4',
            field=models.IntegerField(default=0, help_text='Discount applicable for 2 individual.'),
        ),
    ]
