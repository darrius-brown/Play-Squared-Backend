# Generated by Django 4.0.6 on 2022-08-20 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play_squared', '0006_score_board'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='game',
            field=models.CharField(default='game', max_length=100),
        ),
        migrations.DeleteModel(
            name='Game',
        ),
    ]
