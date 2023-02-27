# Generated by Django 4.0.3 on 2023-02-27 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('limbus', '0002_ego_image_link_identity_image_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_game_id', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=30)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PassiveAbnormality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_game_id', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=30)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PassiveEgo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_game_id', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=30)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PassiveEnemy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_game_id', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=30)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='ego',
            name='skills',
        ),
        migrations.RemoveField(
            model_name='identity',
            name='skills',
        ),
        migrations.AddField(
            model_name='ego',
            name='awakening_skill',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ego',
            name='corrision_skill',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ego',
            name='is_in_game',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='ego',
            name='sinner',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='limbus.sinner'),
        ),
        migrations.AddField(
            model_name='ego',
            name='speed',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='identity',
            name='block',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='identity',
            name='hp',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='identity',
            name='is_in_game',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='identity',
            name='skill_1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='identity',
            name='skill_2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='identity',
            name='skill_3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='identity',
            name='speed',
            field=models.CharField(default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='ego',
            name='resistance_blunt',
            field=models.CharField(choices=[('F', 'Fatal'), ('W', 'Weak'), ('N', 'Normal'), ('E', 'Endured'), ('I', 'Ineffective'), ('M', 'Immune')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='ego',
            name='resistance_envy',
            field=models.CharField(choices=[('F', 'Fatal'), ('W', 'Weak'), ('N', 'Normal'), ('E', 'Endured'), ('I', 'Ineffective'), ('M', 'Immune')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='ego',
            name='resistance_gloom',
            field=models.CharField(choices=[('F', 'Fatal'), ('W', 'Weak'), ('N', 'Normal'), ('E', 'Endured'), ('I', 'Ineffective'), ('M', 'Immune')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='ego',
            name='resistance_gluttony',
            field=models.CharField(choices=[('F', 'Fatal'), ('W', 'Weak'), ('N', 'Normal'), ('E', 'Endured'), ('I', 'Ineffective'), ('M', 'Immune')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='ego',
            name='resistance_lust',
            field=models.CharField(choices=[('F', 'Fatal'), ('W', 'Weak'), ('N', 'Normal'), ('E', 'Endured'), ('I', 'Ineffective'), ('M', 'Immune')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='ego',
            name='resistance_pierce',
            field=models.CharField(choices=[('F', 'Fatal'), ('W', 'Weak'), ('N', 'Normal'), ('E', 'Endured'), ('I', 'Ineffective'), ('M', 'Immune')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='ego',
            name='resistance_pride',
            field=models.CharField(choices=[('F', 'Fatal'), ('W', 'Weak'), ('N', 'Normal'), ('E', 'Endured'), ('I', 'Ineffective'), ('M', 'Immune')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='ego',
            name='resistance_slash',
            field=models.CharField(choices=[('F', 'Fatal'), ('W', 'Weak'), ('N', 'Normal'), ('E', 'Endured'), ('I', 'Ineffective'), ('M', 'Immune')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='ego',
            name='resistance_sloth',
            field=models.CharField(choices=[('F', 'Fatal'), ('W', 'Weak'), ('N', 'Normal'), ('E', 'Endured'), ('I', 'Ineffective'), ('M', 'Immune')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='ego',
            name='resistance_wrath',
            field=models.CharField(choices=[('F', 'Fatal'), ('W', 'Weak'), ('N', 'Normal'), ('E', 'Endured'), ('I', 'Ineffective'), ('M', 'Immune')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='identity',
            name='resistance_blunt',
            field=models.CharField(choices=[('F', 'Fatal'), ('W', 'Weak'), ('N', 'Normal'), ('E', 'Endured'), ('I', 'Ineffective'), ('M', 'Immune')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='identity',
            name='resistance_envy',
            field=models.CharField(choices=[('F', 'Fatal'), ('W', 'Weak'), ('N', 'Normal'), ('E', 'Endured'), ('I', 'Ineffective'), ('M', 'Immune')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='identity',
            name='resistance_gloom',
            field=models.CharField(choices=[('F', 'Fatal'), ('W', 'Weak'), ('N', 'Normal'), ('E', 'Endured'), ('I', 'Ineffective'), ('M', 'Immune')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='identity',
            name='resistance_gluttony',
            field=models.CharField(choices=[('F', 'Fatal'), ('W', 'Weak'), ('N', 'Normal'), ('E', 'Endured'), ('I', 'Ineffective'), ('M', 'Immune')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='identity',
            name='resistance_lust',
            field=models.CharField(choices=[('F', 'Fatal'), ('W', 'Weak'), ('N', 'Normal'), ('E', 'Endured'), ('I', 'Ineffective'), ('M', 'Immune')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='identity',
            name='resistance_pierce',
            field=models.CharField(choices=[('F', 'Fatal'), ('W', 'Weak'), ('N', 'Normal'), ('E', 'Endured'), ('I', 'Ineffective'), ('M', 'Immune')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='identity',
            name='resistance_pride',
            field=models.CharField(choices=[('F', 'Fatal'), ('W', 'Weak'), ('N', 'Normal'), ('E', 'Endured'), ('I', 'Ineffective'), ('M', 'Immune')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='identity',
            name='resistance_slash',
            field=models.CharField(choices=[('F', 'Fatal'), ('W', 'Weak'), ('N', 'Normal'), ('E', 'Endured'), ('I', 'Ineffective'), ('M', 'Immune')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='identity',
            name='resistance_sloth',
            field=models.CharField(choices=[('F', 'Fatal'), ('W', 'Weak'), ('N', 'Normal'), ('E', 'Endured'), ('I', 'Ineffective'), ('M', 'Immune')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='identity',
            name='resistance_wrath',
            field=models.CharField(choices=[('F', 'Fatal'), ('W', 'Weak'), ('N', 'Normal'), ('E', 'Endured'), ('I', 'Ineffective'), ('M', 'Immune')], default='N', max_length=1),
        ),
    ]