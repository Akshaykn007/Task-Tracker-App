# Generated by Django 3.2.5 on 2022-04-17 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskTrackerApp', '0010_auto_20220417_2218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='members',
            name='menu',
        ),
        migrations.CreateModel(
            name='TeamMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='taskTrackerApp.members')),
                ('teamId', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='taskTrackerApp.team')),
            ],
        ),
    ]