# Generated by Django 4.0.3 on 2023-02-27 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('limbus', '0006_ego_awakening_skill_ego_corrision_skill_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ego',
            name='passive_off_field',
        ),
        migrations.RemoveField(
            model_name='ego',
            name='passive_on_field',
        ),
        migrations.RemoveField(
            model_name='identity',
            name='passive_off_field',
        ),
        migrations.RemoveField(
            model_name='identity',
            name='passive_on_field',
        ),
    ]
