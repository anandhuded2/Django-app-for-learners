# Generated by Django 2.0.7 on 2018-07-25 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0002_game_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='move',
            name='by_first_player',
        ),
        migrations.AlterField(
            model_name='game',
            name='status',
            field=models.CharField(choices=[('F', 'First Player To Move'), ('S', 'Second Player To Move'), ('W', 'First Player Wins'), ('L', 'Second Player Wins'), ('D', 'Draw')], default='F', max_length=1),
        ),
        migrations.AlterField(
            model_name='move',
            name='comment',
            field=models.CharField(max_length=300),
        ),
    ]
