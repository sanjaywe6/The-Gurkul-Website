# Generated by Django 4.1.3 on 2022-11-21 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gurkul_test', '0003_gurkul_competition_test_series_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='gurkul_academic_test_series_model',
            name='language',
            field=models.CharField(default='Hindi', max_length=30),
        ),
        migrations.AddField(
            model_name='gurkul_competition_test_series_model',
            name='language',
            field=models.CharField(default='Hindi', max_length=30),
        ),
    ]
