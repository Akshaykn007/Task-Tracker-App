# Generated by Django 3.2.5 on 2022-04-17 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskTrackerApp', '0009_auto_20220417_2214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='item',
            name='menu',
        ),
        migrations.RenameModel(
            old_name='Menu',
            new_name='Team',
        ),
        migrations.DeleteModel(
            name='Drink',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.AddField(
            model_name='members',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskTrackerApp.team'),
        ),
    ]
