# Generated by Django 3.2.5 on 2022-04-17 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskTrackerApp', '0014_auto_20220417_2301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teammembers',
            name='availability',
        ),
        migrations.AddField(
            model_name='members',
            name='availability',
            field=models.BooleanField(max_length=10, null=True),
        ),
    ]