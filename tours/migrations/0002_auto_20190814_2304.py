# Generated by Django 2.2.2 on 2019-08-14 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='category',
        ),
        migrations.RemoveField(
            model_name='package',
            name='destinationtype',
        ),
        migrations.RemoveField(
            model_name='package',
            name='tourfor',
        ),
        migrations.RemoveField(
            model_name='package',
            name='tourtype',
        ),
        migrations.AddField(
            model_name='package',
            name='is_booking_open',
            field=models.BooleanField(default=1, help_text='If ticked, it means the bookings are closed for this sale.'),
        ),
        migrations.AddField(
            model_name='package',
            name='is_couple_only',
            field=models.BooleanField(default=1, help_text='If ticked, it means the package is for couples.'),
        ),
        migrations.AddField(
            model_name='package',
            name='is_expedition',
            field=models.BooleanField(default=1, help_text='If ticked, it means the bookings are closed for this sale.'),
        ),
        migrations.AddField(
            model_name='package',
            name='is_it_group_package',
            field=models.BooleanField(default=1, help_text='If ticked, it means the tour will happen in group.'),
        ),
        migrations.AddField(
            model_name='package',
            name='is_listed',
            field=models.BooleanField(default=1, help_text='If ticked, it means that this sale is live.'),
        ),
        migrations.AddField(
            model_name='package',
            name='is_or_has_trekking',
            field=models.BooleanField(default=1, help_text='If ticked, it means the tour contains some kind of trekking'),
        ),
        migrations.AddField(
            model_name='package',
            name='mention_cities',
            field=models.TextField(default='manali', help_text='Use same name as cities in citylist. eg: new delhi, chandigarh, manali, ...'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='package',
            name='agegroup',
            field=models.CharField(choices=[('all', 'ALL'), ('18', 'ABOVE18')], default='All', max_length=100),
        ),
    ]
