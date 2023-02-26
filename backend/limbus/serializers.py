from .models import Sinner, Identity, EGO
from rest_framework import serializers

class IdentitySerializers(serializers.ModelSerializer):
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
            "resistance_blunt"
        ]
