# Generated by Django 3.2.5 on 2022-04-17 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskTrackerApp', '0018_alter_teammembers_team_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
