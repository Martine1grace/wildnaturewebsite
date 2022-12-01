# Generated by Django 3.1.2 on 2021-10-28 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_dayaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourpackage',
            name='day_actions',
            field=models.ManyToManyField(blank=True, related_name='day_actions', to='core.DayAction'),
        ),
    ]