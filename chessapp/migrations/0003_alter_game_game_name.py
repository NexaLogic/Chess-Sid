# Generated by Django 5.0.1 on 2024-02-05 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chessapp', '0002_game_game_is'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game_name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
