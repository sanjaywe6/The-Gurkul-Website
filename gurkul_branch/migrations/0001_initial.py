# Generated by Django 4.1.2 on 2022-10-21 13:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='branch_teacher_faculty',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('mob', models.BigIntegerField(default=0)),
                ('msg_mob', models.BigIntegerField(default=0)),
                ('sub', models.CharField(max_length=30)),
                ('branch_code', models.CharField(max_length=20)),
                ('join_time', models.TimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
