# Generated by Django 4.0.3 on 2023-03-03 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('limbus', '0014_skill_coin_mod_skill_coin_num_skill_coin_roll_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identity',
            name='base_damage',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='identity',
            name='growth',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
    ]
