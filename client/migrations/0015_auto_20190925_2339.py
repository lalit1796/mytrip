# Generated by Django 2.2.2 on 2019-09-25 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0014_auto_20190925_2338'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='l_name',
            new_name='last_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='f_name',
        ),
        migrations.AddField(
            model_name='order',
            name='first_name',
            field=models.CharField(default='anonymous', help_text='First Name', max_length=200),
        ),
    ]