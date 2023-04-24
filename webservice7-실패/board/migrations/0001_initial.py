# Generated by Django 4.1.7 on 2023-04-20 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Board",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("writer", models.CharField(max_length=30)),
                ("title", models.CharField(max_length=100)),
                ("text", models.CharField(max_length=255)),
                ("cnt", models.BigIntegerField()),
            ],
        ),
    ]
