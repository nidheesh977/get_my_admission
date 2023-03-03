# Generated by Django 4.1.7 on 2023-03-03 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('location', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images/college')),
                ('logo', models.ImageField(upload_to='images/college/logos')),
                ('brochure', models.FileField(upload_to='documents/brochure')),
                ('approved_by', models.CharField(max_length=200)),
                ('view_count', models.IntegerField(default=0)),
                ('course_offered', models.IntegerField()),
                ('total_faculty', models.IntegerField()),
                ('established_in', models.DateField()),
                ('max_package', models.CharField(max_length=200)),
                ('fee_range', models.CharField(max_length=200)),
                ('college_type', models.CharField(default='Public', max_length=200)),
                ('NIRF_Ranking', models.IntegerField()),
                ('short_description', models.TextField()),
                ('reviews_count', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('overview', models.TextField()),
                ('course_list', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CollegeImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/collegeImages')),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colleges.college')),
            ],
        ),
        migrations.CreateModel(
            name='CollegeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('colleges', models.ManyToManyField(blank=True, to='colleges.college')),
            ],
        ),
    ]