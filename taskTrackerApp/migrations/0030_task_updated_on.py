# Generated by Django 3.2.5 on 2022-04-18 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskTrackerApp', '0029_task_task_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='updated_on',
            field=models.DateField(auto_now=True, max_length=30),
        ),
    ]
