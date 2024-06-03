# Generated by Django 5.0.6 on 2024-06-03 22:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_user_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='nazwa',
        ),
        migrations.AddField(
            model_name='task',
            name='deadline',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='task',
            name='level',
            field=models.CharField(default='easy', max_length=100),
        ),
        migrations.AddField(
            model_name='task',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]