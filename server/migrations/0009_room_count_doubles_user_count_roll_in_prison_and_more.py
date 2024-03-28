# Generated by Django 4.2 on 2024-03-18 12:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("server", "0008_rename_player_turn_room_current_player"),
    ]

    operations = [
        migrations.AddField(
            model_name="room",
            name="count_doubles",
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="user",
            name="count_roll_in_prison",
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="user",
            name="in_prison",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="monopoly",
            field=models.CharField(blank=True, default="", max_length=20),
        ),
        migrations.AlterField(
            model_name="room",
            name="current_player",
            field=models.SmallIntegerField(default=0),
        ),
    ]