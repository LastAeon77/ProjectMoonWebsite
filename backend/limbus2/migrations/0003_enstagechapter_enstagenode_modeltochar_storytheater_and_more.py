# Generated by Django 4.1.7 on 2024-09-12 00:10

import django.contrib.postgres.indexes
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("limbus2", "0002_alter_egoattributeresist_value"),
    ]

    operations = [
        migrations.CreateModel(
            name="EnStageChapter",
            fields=[
                (
                    "id",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("company", models.CharField(max_length=100)),
                ("area", models.CharField(max_length=100)),
                ("chapter", models.CharField(max_length=50)),
                ("chapterNumber", models.CharField(max_length=10)),
                ("chaptertitle", models.CharField(max_length=100)),
                ("timeline", models.CharField(max_length=20)),
                ("id_int", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="EnStageNode",
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
                ("title", models.CharField(blank=True, max_length=100, null=True)),
                ("place", models.CharField(blank=True, max_length=100, null=True)),
                ("desc", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="ModelToChar",
            fields=[
                (
                    "id",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("krname", models.CharField(blank=True, max_length=20, null=True)),
                ("jpname", models.CharField(blank=True, max_length=20, null=True)),
                ("enname", models.CharField(blank=True, max_length=20, null=True)),
                ("fileName", models.CharField(blank=True, max_length=50, null=True)),
                ("nickName", models.CharField(blank=True, max_length=50, null=True)),
                ("jpNickName", models.CharField(blank=True, max_length=50, null=True)),
                ("enNickName", models.CharField(blank=True, max_length=50, null=True)),
                ("staringSide", models.CharField(blank=True, max_length=10, null=True)),
                ("bottomYPos", models.IntegerField(blank=True, null=True)),
                (
                    "portraitSpritePath",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "nameTagColor",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="StoryTheater",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("chapter_id", models.IntegerField()),
                ("unlock_condition", models.JSONField(blank=True, null=True)),
                ("sorting_order", models.IntegerField(blank=True, null=True)),
                ("condition", models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="StoryTheaterList",
            fields=[
                (
                    "id",
                    models.CharField(max_length=30, primary_key=True, serialize=False),
                ),
                ("id_index", models.IntegerField()),
                ("node_id", models.IntegerField()),
                ("stageDetail", models.CharField(blank=True, max_length=30, null=True)),
                (
                    "story_theater",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="limbus2.storytheater",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EnLimbusStory",
            fields=[
                (
                    "id",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("id_index", models.FloatField()),
                ("id_raw", models.IntegerField()),
                ("place", models.CharField(blank=True, max_length=100, null=True)),
                ("model", models.CharField(blank=True, max_length=100, null=True)),
                ("teller", models.CharField(blank=True, max_length=100, null=True)),
                ("title", models.CharField(blank=True, max_length=100, null=True)),
                ("content", models.TextField(blank=True, null=True)),
                (
                    "theater_story_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="limbus2.storytheaterlist",
                    ),
                ),
            ],
        ),
        migrations.AddIndex(
            model_name="enlimbusstory",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["content"], name="content_gin_index", opclasses=["gin_trgm_ops"]
            ),
        ),
    ]
