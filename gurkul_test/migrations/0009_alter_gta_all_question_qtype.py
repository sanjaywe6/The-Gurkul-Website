# Generated by Django 4.1.7 on 2023-03-11 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gurkul_test', '0008_remove_all_competition_available_test_series_user_profile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gta_all_question',
            name='qtype',
            field=models.CharField(choices=[('MCQ', 'Multiple Choice Question (MCQ)'), ('STQ', 'Short Type Question (STQ)'), ('LTQ', 'Long Type Question (LTQ)'), ('VLTQ', 'Very Long Type Question (VLTQ)'), ('Other', 'Other')], default='Other', max_length=50),
        ),
    ]
