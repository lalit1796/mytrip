# Generated by Django 2.2.2 on 2019-09-09 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('props', '0004_qlink'),
    ]

    operations = [
        migrations.AddField(
            model_name='qlink',
            name='link_src',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='qlink',
            name='link_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
