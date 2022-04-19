# Generated by Django 3.2.5 on 2022-04-18 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskTrackerApp', '0030_task_updated_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='updated_by',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='task',
            name='updated_on',
            field=models.DateField(blank=True, max_length=30),
        ),
    ]
