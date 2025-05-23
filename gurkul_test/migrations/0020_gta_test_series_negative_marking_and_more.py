# Generated by Django 4.1.7 on 2023-05-17 07:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gurkul_test', '0019_rename_time_gta_test_series_add_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gta_test_series',
            name='negative_marking',
            field=models.IntegerField(choices=[(-0.5, '-1/2 Markin per wrong answer'), (-1.0, '-1 Markin per wrong answer'), (-1.5, '-3/2 Markin per wrong answer'), (-2.0, '-2 Markin per wrong answer')], default=-1.0),
        ),
        migrations.AddField(
            model_name='gta_test_series',
            name='positive_marking',
            field=models.IntegerField(choices=[(0.5, '1/2 Markin per right answer'), (1.0, '1 Markin per right answer'), (1.5, '3/2 Markin per right answer'), (2.0, '2 Markin per right answer'), (2.5, '5/2 Markin per right answer'), (3.0, '3 Markin per right answer')], default=2.0),
        ),
        migrations.AlterField(
            model_name='gta_test_series',
            name='id',
            field=models.CharField(default='GTA0<django.db.models.fields.AutoField>', max_length=15),
        ),
        migrations.AlterField(
            model_name='gta_test_series',
            name='questions_length',
            field=models.IntegerField(choices=[(10, '10 Questions'), (15, '15 Questions'), (20, '20 Questions'), (25, '25 Questions'), (30, '30 Questions'), (35, '35 Questions'), (40, '40 Questions'), (45, '45 Questions'), (50, '50 Questions'), (55, '55 Questions'), (60, '60 Questions'), (65, '65 Questions'), (70, '70 Questions'), (75, '75 Questions'), (80, '80 Questions'), (85, '85 Questions'), (90, '90 Questions'), (95, '95 Questions'), (100, '100 Questions')], default=15),
        ),
        migrations.AlterField(
            model_name='gta_test_series',
            name='time_period',
            field=models.DurationField(choices=[(datetime.timedelta(seconds=900), '15 Minutes'), (datetime.timedelta(seconds=1800), '30 Minutes'), (datetime.timedelta(seconds=2700), '45 Minutes'), (datetime.timedelta(seconds=3600), '1 Hour'), (datetime.timedelta(seconds=5400), '1.5 Hours'), (datetime.timedelta(seconds=7200), '2 Hours'), (datetime.timedelta(seconds=9000), '2.5 Hours'), (datetime.timedelta(seconds=10800), '3 Hours')], default=datetime.timedelta(seconds=1800)),
        ),
        migrations.AlterField(
            model_name='gta_test_series',
            name='total_length',
            field=models.IntegerField(default=0),
        ),
    ]
