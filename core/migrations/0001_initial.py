# Generated by Django 3.1.2 on 2021-10-26 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TourPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(blank=True, max_length=100, null=True)),
                ('package_desc', models.TextField(blank=True, max_length=100, null=True)),
                ('package_slogan', models.CharField(blank=True, max_length=100, null=True)),
                ('main_place', models.CharField(blank=True, max_length=100, null=True)),
                ('days_to_travel', models.IntegerField(blank=True, null=True)),
                ('ratings', models.DecimalField(blank=True, decimal_places=1, max_digits=1, null=True)),
                ('packagePrice', models.DecimalField(decimal_places=2, max_digits=5)),
                ('packageImage', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]