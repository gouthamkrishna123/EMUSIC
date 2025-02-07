# Generated by Django 4.2.6 on 2023-12-06 04:20

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="customer",
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
                ("username", models.CharField(max_length=200)),
                ("name", models.CharField(max_length=200)),
                ("password", models.CharField(max_length=20)),
                ("conformpassword", models.CharField(max_length=20)),
                ("age", models.IntegerField()),
                ("email", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="music",
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
                ("title", models.TextField()),
                ("artist", models.TextField()),
                ("image", models.ImageField(upload_to="pics")),
                ("audio_file", models.FileField(blank=True, null=True, upload_to="")),
                ("audio_link", models.CharField(max_length=500)),
            ],
        ),
    ]
