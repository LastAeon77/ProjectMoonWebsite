from .models import Sinner, Identity, EGO
from rest_framework import serializers


class IdentitySerializers(serializers.ModelSerializer):
    resistance_wrath = serializers.SerializerMethodField()
    resistance_lust = serializers.SerializerMethodField()
    resistance_wrath = serializers.SerializerMethodField()
    resistance_sloth = serializers.SerializerMethodField()
    resistance_gluttony = serializers.SerializerMethodField()
    resistance_gloom = serializers.SerializerMethodField()
    resistance_pride = serializers.SerializerMethodField()
    resistance_envy = serializers.SerializerMethodField()
    resistance_slash = serializers.SerializerMethodField()
    resistance_pierce = serializers.SerializerMethodField()
    resistance_blunt = serializers.SerializerMethodField()
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
    resistance_wrath = serializers.SerializerMethodField()
    resistance_lust = serializers.SerializerMethodField()
    resistance_wrath = serializers.SerializerMethodField()
    resistance_sloth = serializers.SerializerMethodField()
    resistance_gluttony = serializers.SerializerMethodField()
    resistance_gloom = serializers.SerializerMethodField()
    resistance_pride = serializers.SerializerMethodField()
    resistance_envy = serializers.SerializerMethodField()
    resistance_slash = serializers.SerializerMethodField()
    resistance_pierce = serializers.SerializerMethodField()
    resistance_blunt = serializers.SerializerMethodField()
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
