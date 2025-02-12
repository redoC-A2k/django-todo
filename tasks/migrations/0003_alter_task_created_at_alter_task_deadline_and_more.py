# Generated by Django 5.0.6 on 2024-06-13 00:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_task_created_at_alter_task_deadline_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 13, 0, 32, 38, 954826, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='tasks.tag'),
        ),
    ]
