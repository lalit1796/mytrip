# Generated by Django 2.2.2 on 2019-09-28 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0043_activitysale_gst'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitysale',
            name='thumb',
            field=models.ImageField(default=0, help_text='Ideal dimaensions 300 x 240', max_length=255, upload_to='thumbs'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='package',
            name='thumb',
            field=models.ImageField(default=0, help_text='Ideal dimaensions 300 x 240', max_length=255, upload_to='thumbs'),
            preserve_default=False,
        ),
    ]