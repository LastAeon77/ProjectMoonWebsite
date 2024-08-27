# Generated by Django 4.1.7 on 2024-08-26 14:16

from django.db import migrations, models
import django.db.models.deletion
import django_jsonform.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ego",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("egoType", models.CharField(max_length=20)),
                ("egoClass", models.IntegerField(blank=True, null=True)),
                ("season", models.IntegerField(blank=True, null=True)),
                ("skilltier", models.IntegerField(blank=True, null=True)),
                (
                    "additionalAttachment",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                (
                    "walpurgisType",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EgoPassive",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name="EgoSkill",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("skillType", models.CharField(max_length=40)),
                ("skillTier", models.IntegerField()),
                (
                    "requireIDList",
                    django_jsonform.models.fields.ArrayField(
                        base_field=models.CharField(
                            blank=True, max_length=50, null=True
                        ),
                        default=list,
                        size=None,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EnEgoSkillCoinEffect",
            fields=[
                (
                    "id",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("action_index", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Identity",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("appearance", models.TextField(blank=True, null=True)),
                (
                    "unitKeyWordList",
                    django_jsonform.models.fields.ArrayField(
                        base_field=models.CharField(
                            blank=True, max_length=200, null=True
                        ),
                        blank=True,
                        default=list,
                        null=True,
                        size=None,
                    ),
                ),
                (
                    "associationList",
                    django_jsonform.models.fields.ArrayField(
                        base_field=models.CharField(
                            blank=True, max_length=200, null=True
                        ),
                        blank=True,
                        default=list,
                        null=True,
                        size=None,
                    ),
                ),
                (
                    "unitScriptID",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                ("season", models.IntegerField(blank=True, null=True)),
                (
                    "walpurgisType",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "slotWeightConditionList",
                    django_jsonform.models.fields.ArrayField(
                        base_field=models.CharField(
                            blank=True, max_length=200, null=True
                        ),
                        blank=True,
                        null=True,
                        size=10,
                    ),
                ),
                ("rank", models.IntegerField(blank=True, null=True)),
                ("defCorrection", models.IntegerField(blank=True, null=True)),
                (
                    "minSpeedList",
                    django_jsonform.models.fields.ArrayField(
                        base_field=models.IntegerField(blank=True, null=True),
                        blank=True,
                        null=True,
                        size=10,
                    ),
                ),
                (
                    "maxSpeedList",
                    django_jsonform.models.fields.ArrayField(
                        base_field=models.IntegerField(blank=True, null=True),
                        blank=True,
                        null=True,
                        size=10,
                    ),
                ),
                (
                    "uniqueAttribute",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "breakSection",
                    django_jsonform.models.fields.ArrayField(
                        base_field=models.IntegerField(blank=True, null=True),
                        blank=True,
                        null=True,
                        size=5,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PanicType",
            fields=[
                ("panicName", models.CharField(blank=True, max_length=200, null=True)),
                ("lowMoraleDescription", models.TextField(blank=True, null=True)),
                ("panicDescription", models.TextField(blank=True, null=True)),
                ("id", models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name="Passive",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                (
                    "requireIDList",
                    django_jsonform.models.fields.ArrayField(
                        base_field=models.CharField(
                            blank=True, max_length=50, null=True
                        ),
                        default=list,
                        size=None,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Sinner",
            fields=[
                ("name", models.CharField(max_length=200)),
                ("id", models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name="Skill",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("skillType", models.CharField(blank=True, max_length=20, null=True)),
                ("skillTier", models.IntegerField(blank=True, null=True)),
                (
                    "requireIDList",
                    django_jsonform.models.fields.ArrayField(
                        base_field=models.CharField(
                            blank=True, max_length=50, null=True
                        ),
                        default=list,
                        size=None,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Hp",
            fields=[
                ("defaultStat", models.IntegerField()),
                ("incrementByLevel", models.FloatField()),
                (
                    "id",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="limbus2.identity",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SkillData",
            fields=[
                (
                    "id",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("uptie_level", models.IntegerField()),
                (
                    "attribute_type",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("atk_type", models.CharField(blank=True, max_length=50, null=True)),
                ("def_type", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "skill_target_type",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("target_num", models.IntegerField(blank=True, null=True)),
                ("mp_usage", models.IntegerField(blank=True, null=True)),
                ("skill_level_correction", models.FloatField(blank=True, null=True)),
                ("default_value", models.FloatField(blank=True, null=True)),
                ("can_team_kill", models.BooleanField(default=False)),
                ("can_duel", models.BooleanField(default=False)),
                ("can_change_target", models.BooleanField(default=False)),
                (
                    "skill_motion",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("view_type", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "parrying_close_type",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("icon_id", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "skill",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="skill_data",
                        to="limbus2.skill",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RelSkill",
            fields=[
                (
                    "id",
                    models.CharField(max_length=254, primary_key=True, serialize=False),
                ),
                ("skill_num", models.IntegerField()),
                (
                    "identity",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="limbus2.identity",
                    ),
                ),
                (
                    "skill",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="limbus2.skill"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RelPassiveEGO",
            fields=[
                (
                    "id",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                (
                    "is_awakening",
                    models.BooleanField(blank=True, default=True, null=True),
                ),
                (
                    "ego",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="limbus2.ego"
                    ),
                ),
                (
                    "passive",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="limbus2.egopassive",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RelPassive",
            fields=[
                ("uptie_level", models.IntegerField()),
                ("is_support", models.BooleanField(default=False)),
                (
                    "id",
                    models.CharField(max_length=254, primary_key=True, serialize=False),
                ),
                (
                    "identity",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="limbus2.identity",
                    ),
                ),
                (
                    "passive",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="limbus2.passive",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="identity",
            name="characterId",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="limbus2.sinner",
            ),
        ),
        migrations.AddField(
            model_name="identity",
            name="panicType",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="limbus2.panictype",
            ),
        ),
        migrations.AddField(
            model_name="identity",
            name="passive",
            field=models.ManyToManyField(
                through="limbus2.RelPassive", to="limbus2.passive"
            ),
        ),
        migrations.AddField(
            model_name="identity",
            name="skills",
            field=models.ManyToManyField(
                through="limbus2.RelSkill", to="limbus2.skill"
            ),
        ),
        migrations.CreateModel(
            name="EnSkillEffect",
            fields=[
                ("uptie_level", models.IntegerField(blank=True, null=True)),
                ("name", models.CharField(max_length=100)),
                ("desc", models.TextField()),
                (
                    "keywords",
                    django_jsonform.models.fields.ArrayField(
                        base_field=models.CharField(max_length=30),
                        blank=True,
                        default=list,
                        null=True,
                        size=None,
                    ),
                ),
                (
                    "id",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                (
                    "skill",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="en_skill_coin_effect",
                        to="limbus2.skill",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EnPassiveDescription",
            fields=[
                ("name", models.CharField(max_length=100)),
                ("desc", models.TextField()),
                ("summary", models.TextField()),
                (
                    "id",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                (
                    "passive",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="limbus2.passive",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EnIdentityInfo",
            fields=[
                ("title", models.CharField(blank=True, max_length=50, null=True)),
                ("name", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "nameWithTitle",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("desc", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "id",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                (
                    "identity",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="en_info",
                        to="limbus2.identity",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EnEgoSkillEffect",
            fields=[
                (
                    "id",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=50)),
                ("desc", models.TextField(blank=True, null=True)),
                ("uptie_level", models.IntegerField()),
                (
                    "ego_skill",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ego_level_list_en",
                        to="limbus2.egoskill",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EnEgoSkillCoinEffectDesc",
            fields=[
                (
                    "id",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("desc", models.TextField(blank=True, null=True)),
                ("summary", models.TextField(blank=True, null=True)),
                (
                    "ego_skill_coin_effect",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="limbus2.enegoskillcoineffect",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="enegoskillcoineffect",
            name="ego_skill_effect",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="limbus2.enegoskilleffect",
            ),
        ),
        migrations.CreateModel(
            name="EnEgoPassive",
            fields=[
                (
                    "id",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(blank=True, max_length=50, null=True)),
                ("desc", models.TextField(blank=True, null=True)),
                (
                    "ego_passive",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="limbus2.egopassive",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EnEgoInfo",
            fields=[
                (
                    "id",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(blank=True, max_length=50, null=True)),
                ("desc", models.TextField(blank=True, null=True)),
                (
                    "ego",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="limbus2.ego"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EnCoinEffectList",
            fields=[
                (
                    "id",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("action_index", models.IntegerField()),
                (
                    "skill_coin_effect",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="en_coin_effect",
                        to="limbus2.enskilleffect",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EnCoinEffectDesc",
            fields=[
                (
                    "id",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("desc", models.TextField(blank=True, null=True)),
                ("summary", models.TextField(blank=True, null=True)),
                (
                    "coin",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="en_coin_desc",
                        to="limbus2.encoineffectlist",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EgoSkillData",
            fields=[
                (
                    "id",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("uptie_level", models.IntegerField()),
                (
                    "attribute_type",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("atk_type", models.CharField(blank=True, max_length=50, null=True)),
                ("def_type", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "skill_target_type",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("target_num", models.IntegerField(blank=True, null=True)),
                ("mp_usage", models.IntegerField(blank=True, null=True)),
                ("skill_level_correction", models.FloatField(blank=True, null=True)),
                ("default_value", models.FloatField(blank=True, null=True)),
                ("can_team_kill", models.BooleanField(default=False)),
                ("can_duel", models.BooleanField(default=False)),
                ("can_change_target", models.BooleanField(default=False)),
                (
                    "skill_motion",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("view_type", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "parrying_close_type",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("icon_id", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "ego_skill",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ego_skill_data",
                        to="limbus2.egoskill",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EgoRequirement",
            fields=[
                (
                    "id",
                    models.CharField(max_length=30, primary_key=True, serialize=False),
                ),
                ("attributeType", models.CharField(max_length=30)),
                ("num", models.IntegerField()),
                (
                    "ego",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="limbus2.ego"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EgoCorrosionSection",
            fields=[
                (
                    "id",
                    models.CharField(max_length=30, primary_key=True, serialize=False),
                ),
                ("section", models.FloatField()),
                ("probability", models.FloatField()),
                (
                    "ego",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="limbus2.ego"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EgoCoinList",
            fields=[
                ("operator_type", models.CharField(max_length=50)),
                ("scale", models.FloatField(blank=True, null=True)),
                ("action_index", models.IntegerField()),
                (
                    "id",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                (
                    "ego_skill_data",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="EGO_coin_list",
                        to="limbus2.egoskilldata",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EgoAttributeResist",
            fields=[
                (
                    "id",
                    models.CharField(max_length=30, primary_key=True, serialize=False),
                ),
                ("type", models.CharField(max_length=20)),
                ("value", models.IntegerField(blank=True, null=True)),
                (
                    "ego",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="limbus2.ego"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="ego",
            name="awakeningSkillId",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="awakening_ego_skill",
                to="limbus2.egoskill",
            ),
        ),
        migrations.AddField(
            model_name="ego",
            name="characterId",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="limbus2.sinner"
            ),
        ),
        migrations.AddField(
            model_name="ego",
            name="corrosionSkillId",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="corrosion_ego_skill",
                to="limbus2.egoskill",
            ),
        ),
        migrations.AddField(
            model_name="ego",
            name="passive",
            field=models.ManyToManyField(
                through="limbus2.RelPassiveEGO", to="limbus2.egopassive"
            ),
        ),
        migrations.CreateModel(
            name="CoinList",
            fields=[
                ("operator_type", models.CharField(max_length=50)),
                ("scale", models.FloatField(blank=True, null=True)),
                ("action_index", models.IntegerField()),
                (
                    "id",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                (
                    "skill_data",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="coin_list",
                        to="limbus2.skilldata",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AttributeCondition",
            fields=[
                (
                    "id",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("sinType", models.CharField(max_length=50)),
                ("value", models.IntegerField()),
                (
                    "attribute_type",
                    models.CharField(
                        choices=[("stock", "Stock"), ("resonance", "Resonance")],
                        max_length=10,
                    ),
                ),
                (
                    "passive",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="limbus2.passive",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AttackResistList",
            fields=[
                ("atk_type", models.CharField(blank=True, max_length=30, null=True)),
                ("value", models.FloatField()),
                (
                    "id",
                    models.CharField(max_length=254, primary_key=True, serialize=False),
                ),
                (
                    "identity",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="limbus2.identity",
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="relskill",
            constraint=models.UniqueConstraint(
                fields=("identity", "skill"), name="unique_identity_skill_combination"
            ),
        ),
    ]