# Generated by Django 3.2.5 on 2022-04-19 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskTrackerApp', '0034_team_teamleader'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='teamLeader',
        ),
    ]
