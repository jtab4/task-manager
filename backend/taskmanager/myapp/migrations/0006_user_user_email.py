# Generated by Django 5.0.6 on 2024-06-04 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_task_nazwa_task_deadline_task_level_task_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_email',
            field=models.CharField(default='', max_length=100),
        ),
    ]
