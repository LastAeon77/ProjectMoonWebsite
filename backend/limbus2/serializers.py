from rest_framework import serializers
from .models import (
    Identity,
    Passive,
    Sinner,
    PanicType,
    Skill,
    EnSkillEffect,
    EnCoinEffectList,
    EnCoinEffectDesc,
    SkillData,
    RelPassive,
    RelSkill,
    AttributeCondition,
    EnPassiveDescription,
    CoinList,
    EnIdentityInfo,
    Hp,
    AttackResistList)

# class IdentityLite:
#     def __init__(self, title, name, identity):
#         self.title = title
#         self.name = name
#         self.identity = identity

class IdentityListLiteSerializerEN(serializers.Serializer):
    name = serializers.CharField()
    title = serializers.CharField()
    identity = serializers.IntegerField()

class SkillSerializer(serializers.Serializer):
    name = serializers.CharField()
    uptie_level = serializers.CharField()
    defaultRoll = serializers.IntegerField()
    sin_type = serializers.CharField()
    on_use_desc = serializers.CharField()
    coin_effect_list = serializers.ListField(child = serializers.CharField())
    scale = serializers.ListField(child = serializers.IntegerField())
        
    


class IdentitySerializer(serializers.Serializer):
    name = serializers.CharField()
    keywordList = serializers.ListField(child = serializers.CharField())
    assoicationList = serializers.ListField(child = serializers.CharField())
    characterId = serializers.CharField()
    panicType = serializers.CharField()
    defCorrection = serializers.IntegerField()
    rarity = serializers.IntegerField()
    minSpeedList = serializers.ListField(child = serializers.IntegerField())
    maxSpeedList = serializers.ListField(child = serializers.IntegerField())
    breakSection = serializers.ListField(child = serializers.IntegerField())
    hp_default = serializers.IntegerField()
    hp_increment = serializers.FloatField()
