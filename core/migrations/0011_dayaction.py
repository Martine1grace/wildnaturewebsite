# Generated by Django 3.1.2 on 2021-10-28 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20211028_1118'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_title', models.CharField(blank=True, max_length=255, null=True)),
                ('place_name', models.CharField(blank=True, max_length=255, null=True)),
                ('day_desc', models.TextField(blank=True, null=True)),
                ('day_image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
