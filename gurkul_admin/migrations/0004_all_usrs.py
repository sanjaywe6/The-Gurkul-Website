# Generated by Django 3.2.13 on 2022-10-29 02:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gurkul_admin', '0003_users_registration'),
    ]

    operations = [
        migrations.CreateModel(
            name='all_usrs',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=40)),
                ('branch_code', models.CharField(default='', max_length=20, null=True)),
                ('user_id', models.CharField(default='', max_length=20, null=True)),
                ('teacher_id', models.CharField(default='', max_length=20, null=True)),
                ('visitor_type', models.CharField(max_length=40)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('userProfile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
