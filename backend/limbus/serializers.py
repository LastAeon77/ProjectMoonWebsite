from .models import Sinner, Identity, EGO
from rest_framework import serializers


class IdentitySerializers(serializers.ModelSerializer):
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
        model = Identity
        fields = [
            "name",
            "rarity",
            "sinner",
            "passive_on_field",
            "passive_off_field",
            "skills",
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
        ]


class EGOSerializers(serializers.ModelSerializer):
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
            "skills",
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
        ]
