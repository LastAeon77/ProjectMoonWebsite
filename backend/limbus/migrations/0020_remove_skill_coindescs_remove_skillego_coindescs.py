# Generated by Django 4.1.7 on 2023-04-11 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("limbus", "0019_skillego_character"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="skill",
            name="coindescs",
        ),
        migrations.RemoveField(
            model_name="skillego",
            name="coindescs",
        ),
    ]
