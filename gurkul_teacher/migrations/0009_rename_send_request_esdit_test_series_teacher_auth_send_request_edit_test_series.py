# Generated by Django 4.1.7 on 2023-04-26 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gurkul_teacher', '0008_teacher_auth_send_request_esdit_test_series'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher_auth',
            old_name='send_request_esdit_test_series',
            new_name='send_request_edit_test_series',
        ),
    ]
