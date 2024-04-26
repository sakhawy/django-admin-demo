# Generated by Django 4.0.dev20210605162040 on 2021-06-06 12:37

import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Artist",
            fields=[
                (
                    "id",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Release",
            fields=[
                (
                    "id",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("album", "Album"),
                            ("compilation", "Compilation"),
                            ("single", "Single Or Ep"),
                        ],
                        max_length=255,
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("release_date", models.DateField()),
                (
                    "artist",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="releases",
                        to="demo.artist",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Track",
            fields=[
                (
                    "id",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
                ("title", models.CharField(max_length=255)),
                (
                    "artists",
                    models.ManyToManyField(related_name="tracks", to="demo.Artist"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ReleaseTrack",
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
                ("track_number", models.PositiveIntegerField()),
                (
                    "release",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="demo.release"
                    ),
                ),
                (
                    "track",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="demo.track"
                    ),
                ),
            ],
        ),
    ]
