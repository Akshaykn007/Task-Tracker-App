# Generated by Django 3.2.5 on 2022-04-17 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskTrackerApp', '0017_alter_teammembers_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammembers',
            name='team_id',
            field=models.IntegerField(max_length=30, null=True),
        ),
    ]