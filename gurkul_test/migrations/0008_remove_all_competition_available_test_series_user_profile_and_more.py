# Generated by Django 4.1.7 on 2023-03-11 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gurkul_test', '0007_auto_20230305_0709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='all_competition_available_test_series',
            name='user_profile',
        ),
        migrations.DeleteModel(
            name='all_academic_available_test_series',
        ),
        migrations.DeleteModel(
            name='all_competition_available_test_series',
        ),
    ]
