from .models import (
    Sinner,
    Identity,
    EGO,
    Passive,
    PassiveEgo,
    Skill,
    SkillEgo,
    BattleKeywords,
)
from rest_framework import serializers


class SkillSerializers(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class SkillEgoSerializers(serializers.ModelSerializer):
    emotion_type = serializers.CharField(source="get_emotion_type_display")
    character = serializers.StringRelatedField(allow_null=True)
    class Meta:
        model = SkillEgo
        fields = [
            "name",
            "in_game_id",
            "level",
            "character"
            "emotion_type",
            "desc",
            "abName",
            "coindescs",
            "coin_num",
            "coin_roll",
            "coin_mod",
            "type",
            "damage_type",
        ]


class PassiveSerializers(serializers.ModelSerializer):
    class Meta:
        model = Passive
        fields = "__all__"


class PassiveEgoSerializers(serializers.ModelSerializer):
    class Meta:
        model = PassiveEgo
        fields = "__all__"


class BattleKeywordsSerializers(serializers.ModelSerializer):
    class Meta:
        model = BattleKeywords
        fields = "__all__"


class IdentitySerializers(serializers.ModelSerializer):
    skill_1 = serializers.StringRelatedField(allow_null=True)
    skill_2 = serializers.StringRelatedField(allow_null=True)
    skill_3 = serializers.StringRelatedField(allow_null=True)
    passive_on_field = serializers.StringRelatedField(allow_null=True)
    passive_off_field = serializers.StringRelatedField(allow_null=True)
    # resistance_wrath = serializers.CharField(source="get_resistance_wrath_display")
    # resistance_lust = serializers.CharField(source="get_resistance_lust_display")
    # resistance_sloth = serializers.CharField(source="get_resistance_sloth_display")
    # resistance_gluttony = serializers.CharField(
    #     source="get_resistance_gluttony_display"
    # )
    # resistance_gloom = serializers.CharField(source="get_resistance_gloom_display")
    # resistance_pride = serializers.CharField(source="get_resistance_pride_display")
    # resistance_envy = serializers.CharField(source="get_resistance_envy_display")
    resistance_slash = serializers.CharField(source="get_resistance_slash_display")
    resistance_pierce = serializers.CharField(source="get_resistance_pierce_display")
    resistance_blunt = serializers.CharField(source="get_resistance_blunt_display")
    sinner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Identity
        fields = [
            "name",
            "rarity",
            "sinner",
            "hp",
            "block",
            "speed",
            "passive_on_field",
            "passive_off_field",
            "growth",
            "affinity",
            "base_damage",
            "skill_1",
            "skill_1_count",
            "skill_2",
            "skill_2_count",
            "skill_3",
            "skill_3_count",
            # "resistance_wrath",
            # "resistance_lust",
            # "resistance_sloth",
            # "resistance_gluttony",
            # "resistance_gloom",
            # "resistance_pride",
            # "resistance_envy",
            "resistance_slash",
            "resistance_pierce",
            "resistance_blunt",
            "image_link",
        ]


class EGOSerializers(serializers.ModelSerializer):
    awakening_skill = serializers.StringRelatedField(allow_null=True)
    corrision_skill = serializers.StringRelatedField(allow_null=True)
    passive_on_field = serializers.StringRelatedField(allow_null=True)
    passive_off_field = serializers.StringRelatedField(allow_null=True)
    resistance_wrath = serializers.CharField(source="get_resistance_wrath_display")
    resistance_lust = serializers.CharField(source="get_resistance_lust_display")
    resistance_sloth = serializers.CharField(source="get_resistance_sloth_display")
    resistance_gluttony = serializers.CharField(
        source="get_resistance_gluttony_display"
    )
    resistance_gloom = serializers.CharField(source="get_resistance_gloom_display")
    resistance_pride = serializers.CharField(source="get_resistance_pride_display")
    resistance_envy = serializers.CharField(source="get_resistance_envy_display")
    resistance_slash = serializers.CharField(source="get_resistance_slash_display")
    resistance_pierce = serializers.CharField(source="get_resistance_pierce_display")
    resistance_blunt = serializers.CharField(source="get_resistance_blunt_display")
    sinner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = EGO
        fields = [
            "name",
            "rarity",
            "sinner",
            "passive_on_field",
            "passive_off_field",
            "awakening_skill",
            "corrision_skill",
            "resistance_wrath",
            "resistance_lust",
            "resistance_sloth",
            "resistance_gluttony",
            "resistance_gloom",
            "resistance_pride",
            "resistance_envy",
            "resistance_slash",
            "resistance_pierce",
            "resistance_blunt",
            "image_link",
        ]
