# Generated by Django 4.2 on 2024-03-12 04:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("server", "0006_alter_user_pos"),
    ]

    operations = [
        migrations.AddField(
            model_name="room",
            name="start_game",
            field=models.BooleanField(default=False),
        ),
    ]
