# Generated by Django 5.0.6 on 2024-06-04 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_user_user_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_email',
        ),
        migrations.AddField(
            model_name='task',
            name='email_user',
            field=models.CharField(default='', max_length=100),
        ),
    ]