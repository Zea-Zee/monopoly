# Generated by Django 4.2 on 2024-02-19 03:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("server", "0002_alter_user_room"),
    ]

    operations = [
        migrations.AddField(
            model_name="cell",
            name="pawn",
            field=models.BooleanField(default=False),
        ),
    ]
