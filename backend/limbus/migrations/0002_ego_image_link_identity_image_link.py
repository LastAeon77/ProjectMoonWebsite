# Generated by Django 4.0.3 on 2023-02-26 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('limbus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ego',
            name='image_link',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='identity',
            name='image_link',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
