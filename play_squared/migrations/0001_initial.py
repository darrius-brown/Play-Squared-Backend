# Generated by Django 4.0.6 on 2022-07-23 06:27

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='game_name', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='GameRecommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(auto_created=True, default=uuid.uuid3, unique=True)),
                ('user_string', models.CharField(default='unknown_user', max_length=100)),
                ('game_name', models.CharField(default='new_game', max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_string', models.CharField(default='unknown_user', max_length=100)),
                ('amount', models.CharField(max_length=100)),
                ('game', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='scores', to='play_squared.game')),
            ],
        ),
    ]
