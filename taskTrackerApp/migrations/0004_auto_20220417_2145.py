# Generated by Django 3.2.5 on 2022-04-17 16:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taskTrackerApp', '0003_auto_20220417_2142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='Members',
        ),
        migrations.AddField(
            model_name='team',
            name='Members',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]