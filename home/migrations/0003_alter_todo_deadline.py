# Generated by Django 5.0.6 on 2024-07-01 15:13

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_status_todo_status_rename_task_todo_task_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='deadline',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
