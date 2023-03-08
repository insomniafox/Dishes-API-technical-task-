# Generated by Django 4.1.7 on 2023-03-08 22:01

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DishMenu",
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
                (
                    "eating_time",
                    models.CharField(
                        choices=[
                            ("завтрак", "Завтрак"),
                            ("обед", "Обед"),
                            ("ужин", "Ужин"),
                        ],
                        max_length=7,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Menu",
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
                (
                    "day_of_week",
                    models.CharField(
                        choices=[
                            ("monday", "Monday"),
                            ("tuesday", "Tuesday"),
                            ("wednesday", "Wednesday"),
                            ("thursday", "Thursday"),
                            ("friday", "Friday"),
                            ("saturday", "Saturday"),
                            ("sunday", "Sunday"),
                        ],
                        max_length=20,
                        verbose_name="День недели",
                    ),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Меню",
            },
        ),
    ]