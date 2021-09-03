# Generated by Django 2.2.2 on 2019-08-14 16:58

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiling', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_title', models.SlugField(max_length=200)),
                ('package_title', models.CharField(max_length=200)),
                ('intro', models.TextField(null=True)),
                ('insight', models.TextField(null=True)),
                ('generalprize', models.IntegerField(default=0)),
                ('discount', models.IntegerField(default=0)),
                ('costingprize', models.IntegerField(default=0)),
                ('highlight', models.TextField()),
                ('inclusion', models.TextField()),
                ('exclusion', models.TextField()),
                ('city', models.TextField(default=0)),
                ('category', models.TextField()),
                ('agegroup', models.CharField(choices=[('all', 'ALL'), ('18', 'ABOVE18')], default='AllAgeGroup', max_length=100)),
                ('destinationtype', models.TextField()),
                ('tourfor', models.TextField()),
                ('tourtype', models.TextField()),
                ('requirement', models.TextField(blank=True, null=True)),
                ('advisory', models.TextField(blank=True, null=True)),
                ('thingstocarry', models.TextField(blank=True, null=True)),
                ('ameneties', models.TextField(blank=True, null=True)),
                ('disclaimer', models.TextField(blank=True, null=True)),
                ('keywords', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ActivitySale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_booking_open', models.BooleanField(default=1, help_text='If ticked, it means the bookings are closed for this sale.')),
                ('is_listed', models.BooleanField(default=1, help_text='If ticked, it means that this sale is live.')),
                ('intro', models.TextField()),
                ('prize', models.IntegerField(default=0)),
                ('highlight', models.TextField()),
                ('inclusion', models.TextField(blank=True, null=True)),
                ('exclusion', models.TextField(blank=True, null=True)),
                ('agegroup', models.CharField(choices=[('all', 'ALL'), ('18', 'ABOVE18')], default='AllAgeGroup', max_length=100)),
                ('vendor', models.TextField(default='none')),
                ('requirement', models.TextField(blank=True, null=True)),
                ('advisory', models.TextField(blank=True, null=True)),
                ('disclaimer', models.TextField(blank=True, null=True)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(blank=True, help_text='For Additional informations', null=True)),
                ('keywords', models.TextField()),
                ('featured_img_1', models.ImageField(max_length=255, upload_to='saleImg/')),
                ('featured_title_1', models.CharField(max_length=200)),
                ('featured_img_2', models.ImageField(max_length=255, upload_to='saleImg/')),
                ('featured_title_2', models.CharField(max_length=200)),
                ('featured_img_3', models.ImageField(max_length=255, upload_to='saleImg/')),
                ('featured_title_3', models.CharField(max_length=200)),
                ('featured_img_4', models.ImageField(max_length=255, upload_to='saleImg/')),
                ('featured_title_4', models.CharField(max_length=200)),
                ('featured_img_5', models.ImageField(blank=True, max_length=255, null=True, upload_to='saleImg/')),
                ('featured_title_5', models.CharField(blank=True, max_length=200, null=True)),
                ('featured_img_6', models.ImageField(blank=True, max_length=255, null=True, upload_to='saleImg/')),
                ('featured_title_6', models.CharField(blank=True, max_length=200, null=True)),
                ('featured_img_7', models.ImageField(blank=True, max_length=255, null=True, upload_to='saleImg/')),
                ('featured_title_7', models.CharField(blank=True, max_length=200, null=True)),
                ('featured_img_8', models.ImageField(blank=True, max_length=255, null=True, upload_to='saleImg/')),
                ('featured_title_8', models.CharField(blank=True, max_length=200, null=True)),
                ('featured_img_9', models.ImageField(blank=True, max_length=255, null=True, upload_to='saleImg/')),
                ('featured_title_9', models.CharField(blank=True, max_length=200, null=True)),
                ('featured_img_10', models.ImageField(blank=True, max_length=255, null=True, upload_to='saleImg/')),
                ('featured_title_10', models.CharField(blank=True, max_length=200, null=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='name', to='profiling.Activity')),
            ],
        ),
    ]
