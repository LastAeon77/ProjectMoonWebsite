from django.db import models
from django_jsonform.models.fields import ArrayField
from django.contrib.postgres.indexes import GinIndex

# Create your models here.


class Sinner(models.Model):
    name = models.CharField(max_length=200)
    id = models.IntegerField(primary_key=True)


class PanicType(models.Model):
    panicName = models.CharField(max_length=200, null=True, blank=True)
    lowMoraleDescription = models.TextField(null=True, blank=True)
    panicDescription = models.TextField(null=True, blank=True)
    id = models.IntegerField(primary_key=True)


class Passive(models.Model):
    id = models.IntegerField(primary_key=True)
    requireIDList = ArrayField(
        models.CharField(max_length=50, blank=True, null=True), default=list
    )


class AttributeCondition(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    passive = models.ForeignKey(Passive, on_delete=models.CASCADE)
    sinType = models.CharField(max_length=50)
    value = models.IntegerField()
    attribute_type = models.CharField(
        max_length=10, choices=[("stock", "Stock"), ("resonance", "Resonance")]
    )


class EnPassiveDescription(models.Model):
    passive = models.ForeignKey(Passive, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    desc = models.TextField()
    summary = models.TextField()
    id = models.CharField(max_length=50, primary_key=True)


class Skill(models.Model):
    id = models.IntegerField(primary_key=True)
    skillType = models.CharField(max_length=20, null=True, blank=True)
    skillTier = models.IntegerField(null=True, blank=True)
    requireIDList = ArrayField(
        models.CharField(max_length=50, blank=True, null=True), default=list
    )


class EnSkillEffect(models.Model):
    skill = models.ForeignKey(
        Skill, on_delete=models.CASCADE, related_name="en_skill_coin_effect"
    )
    uptie_level = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=200)
    desc = models.TextField()
    keywords = ArrayField(
        models.CharField(max_length=30), null=True, blank=True, default=list
    )
    # id = Skill_id + uptie_level + name
    id = models.CharField(max_length=100, primary_key=True)


class EnCoinEffectList(models.Model):
    # id = skillcoineffect id + action_index
    id = models.CharField(max_length=50, primary_key=True)
    skill_coin_effect = models.ForeignKey(
        EnSkillEffect,
        on_delete=models.CASCADE,
        related_name="en_coin_effect",
        null=True,
        blank=True,
    )
    action_index = models.IntegerField()


class EnCoinEffectDesc(models.Model):
    # id = coineffectlist id * 97
    id = models.CharField(max_length=50, primary_key=True)
    coin = models.ForeignKey(
        EnCoinEffectList,
        on_delete=models.CASCADE,
        related_name="en_coin_desc",
        null=True,
        blank=True,
    )
    desc = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)


class SkillData(models.Model):
    skill = models.ForeignKey(
        Skill, on_delete=models.CASCADE, related_name="skill_data"
    )
    # skill_data id = skill_id_uptie_level
    id = models.CharField(max_length=50, primary_key=True)
    uptie_level = models.IntegerField()
    attribute_type = models.CharField(max_length=50, blank=True, null=True)
    atk_type = models.CharField(max_length=50, blank=True, null=True)
    def_type = models.CharField(max_length=50, blank=True, null=True)
    skill_target_type = models.CharField(max_length=50, blank=True, null=True)
    target_num = models.IntegerField(blank=True, null=True)
    mp_usage = models.IntegerField(blank=True, null=True)
    skill_level_correction = models.FloatField(blank=True, null=True)
    default_value = models.FloatField(blank=True, null=True)
    can_team_kill = models.BooleanField(default=False)
    can_duel = models.BooleanField(default=False)
    can_change_target = models.BooleanField(default=False)
    skill_motion = models.CharField(max_length=50, blank=True, null=True)
    view_type = models.CharField(max_length=50, blank=True, null=True)
    parrying_close_type = models.CharField(max_length=50, blank=True, null=True)
    icon_id = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"SkillData for {self.skill.id} at Uptie Level {self.uptie_level}"


class CoinList(models.Model):
    skill_data = models.ForeignKey(
        SkillData, on_delete=models.CASCADE, related_name="coin_list"
    )
    operator_type = models.CharField(max_length=50)
    scale = models.FloatField(null=True, blank=True)
    action_index = models.IntegerField()
    # id = skill_data id_index of coin
    id = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return f"CoinList for SkillData {self.skill_data.id}"


class Identity(models.Model):
    id = models.IntegerField(primary_key=True)
    appearance = models.TextField(null=True, blank=True)
    unitKeyWordList = ArrayField(
        models.CharField(max_length=200, blank=True, null=True),
        default=list,
        null=True,
        blank=True,
    )
    associationList = ArrayField(
        models.CharField(max_length=200, blank=True, null=True),
        default=list,
        null=True,
        blank=True,
    )
    characterId = models.ForeignKey(
        Sinner, on_delete=models.CASCADE, null=True, blank=True
    )
    panicType = models.ForeignKey(
        PanicType, on_delete=models.CASCADE, null=True, blank=True
    )
    unitScriptID = models.CharField(max_length=30, null=True, blank=True)
    season = models.IntegerField(null=True, blank=True)
    walpurgisType = models.CharField(max_length=50, null=True, blank=True)
    # keep this for another table
    # defenseSkillIDList = ArrayField()
    # panicSkillOnErosion = models.ForeignKey(Skill,on_delete=models.CASCADE)
    slotWeightConditionList = ArrayField(
        models.CharField(max_length=200, blank=True, null=True),
        size=10,
        null=True,
        blank=True,
    )
    # rarity
    rank = models.IntegerField(null=True, blank=True)
    defCorrection = models.IntegerField(null=True, blank=True)
    minSpeedList = ArrayField(
        models.IntegerField(null=True, blank=True), size=10, null=True, blank=True
    )
    maxSpeedList = ArrayField(
        models.IntegerField(null=True, blank=True), size=10, null=True, blank=True
    )
    uniqueAttribute = models.CharField(max_length=50, null=True, blank=True)
    breakSection = ArrayField(
        models.IntegerField(null=True, blank=True), size=5, null=True, blank=True
    )
    passive = models.ManyToManyField(Passive, through="RelPassive")
    skills = models.ManyToManyField(Skill, through="RelSkill")
    # skill will be offboard to another table. Probably a table that can also add attributes in hopefully.


class EnIdentityInfo(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    nameWithTitle = models.CharField(max_length=100, null=True, blank=True)
    desc = models.CharField(max_length=50, null=True, blank=True)
    identity = models.ForeignKey(
        Identity, on_delete=models.CASCADE, related_name="en_info"
    )
    # identity_id_EN
    id = models.CharField(max_length=50, primary_key=True)


class Hp(models.Model):
    defaultStat = models.IntegerField()
    incrementByLevel = models.FloatField()
    id = models.OneToOneField(Identity, on_delete=models.CASCADE, primary_key=True)


class AttackResistList(models.Model):
    atk_type = models.CharField(max_length=30, null=True, blank=True)
    value = models.FloatField()
    id = models.CharField(max_length=254, primary_key=True)
    identity = models.ForeignKey(
        Identity, on_delete=models.CASCADE, null=True, blank=True
    )


class RelPassive(models.Model):
    identity = models.ForeignKey(Identity, on_delete=models.CASCADE)
    passive = models.ForeignKey(Passive, on_delete=models.CASCADE)
    uptie_level = models.IntegerField()
    is_support = models.BooleanField(default=False)
    id = models.CharField(max_length=254, primary_key=True)


class RelSkill(models.Model):
    # id = f'{base["id"]}_{base_attkResistList["atk_type"]}_{base_attkResistList["value"]}'
    id = models.CharField(max_length=254, primary_key=True)
    identity = models.ForeignKey(Identity, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    skill_num = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["identity", "skill"], name="unique_identity_skill_combination"
            )
        ]


############################## EGO #######################################################
class EgoSkill(models.Model):
    id = models.IntegerField(primary_key=True)
    skillType = models.CharField(max_length=40)
    skillTier = models.IntegerField()
    requireIDList = ArrayField(
        models.CharField(max_length=50, blank=True, null=True), default=list
    )


class EgoSkillData(models.Model):
    ego_skill = models.ForeignKey(
        EgoSkill, on_delete=models.CASCADE, related_name="ego_skill_data"
    )
    # skill_data id = skill_id_uptie_level
    id = models.CharField(max_length=50, primary_key=True)
    uptie_level = models.IntegerField()
    attribute_type = models.CharField(max_length=50, blank=True, null=True)
    atk_type = models.CharField(max_length=50, blank=True, null=True)
    def_type = models.CharField(max_length=50, blank=True, null=True)
    skill_target_type = models.CharField(max_length=50, blank=True, null=True)
    target_num = models.IntegerField(blank=True, null=True)
    mp_usage = models.IntegerField(blank=True, null=True)
    skill_level_correction = models.FloatField(blank=True, null=True)
    default_value = models.FloatField(blank=True, null=True)
    can_team_kill = models.BooleanField(default=False)
    can_duel = models.BooleanField(default=False)
    can_change_target = models.BooleanField(default=False)
    skill_motion = models.CharField(max_length=50, blank=True, null=True)
    view_type = models.CharField(max_length=50, blank=True, null=True)
    parrying_close_type = models.CharField(max_length=50, blank=True, null=True)
    icon_id = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.id}"


class EgoCoinList(models.Model):
    ego_skill_data = models.ForeignKey(
        EgoSkillData, on_delete=models.CASCADE, related_name="EGO_coin_list"
    )
    operator_type = models.CharField(max_length=50)
    scale = models.FloatField(null=True, blank=True)
    action_index = models.IntegerField()
    # id = skill_data id_index of coin
    id = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return f"CoinList for SkillData {self.id}"


class EnEgoSkillEffect(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    ego_skill = models.ForeignKey(
        EgoSkill, on_delete=models.CASCADE, related_name="ego_level_list_en"
    )
    name = models.CharField(max_length=50)
    desc = models.TextField(null=True, blank=True)
    uptie_level = models.IntegerField()


class EnEgoSkillCoinEffect(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    ego_skill_effect = models.ForeignKey(
        EnEgoSkillEffect, on_delete=models.CASCADE, null=True, blank=True
    )
    action_index = models.IntegerField()


class EnEgoSkillCoinEffectDesc(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    desc = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    ego_skill_coin_effect = models.ForeignKey(
        EnEgoSkillCoinEffect, on_delete=models.CASCADE, null=True, blank=True
    )


class EgoPassive(models.Model):
    id = models.IntegerField(primary_key=True)


class EnEgoPassive(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    ego_passive = models.ForeignKey(
        EgoPassive, on_delete=models.CASCADE, null=True, blank=True
    )
    name = models.CharField(max_length=50, blank=True, null=True)
    desc = models.TextField(null=True, blank=True)


class Ego(models.Model):
    id = models.IntegerField(primary_key=True)
    characterId = models.ForeignKey(Sinner, on_delete=models.CASCADE)
    egoType = models.CharField(max_length=20)
    egoClass = models.IntegerField(null=True, blank=True)
    season = models.IntegerField(null=True, blank=True)
    skilltier = models.IntegerField(null=True, blank=True)
    additionalAttachment = models.CharField(max_length=20, null=True, blank=True)
    walpurgisType = models.CharField(max_length=20, null=True, blank=True)
    passive = models.ManyToManyField(EgoPassive, through="RelPassiveEGO")
    awakeningSkillId = models.ForeignKey(
        EgoSkill,
        on_delete=models.CASCADE,
        related_name="awakening_ego_skill",
        null=True,
        blank=True,
    )
    corrosionSkillId = models.ForeignKey(
        EgoSkill,
        on_delete=models.CASCADE,
        related_name="corrosion_ego_skill",
        null=True,
        blank=True,
    )


class EnEgoInfo(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    ego = models.ForeignKey(Ego, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)
    desc = models.TextField(null=True, blank=True)


class EgoAttributeResist(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    type = models.CharField(max_length=20)
    value = models.FloatField(null=True, blank=True)
    ego = models.ForeignKey(Ego, on_delete=models.CASCADE)


class EgoRequirement(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    attributeType = models.CharField(max_length=30)
    num = models.IntegerField()
    ego = models.ForeignKey(Ego, on_delete=models.CASCADE)


class EgoCorrosionSection(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    section = models.FloatField()
    probability = models.FloatField()
    ego = models.ForeignKey(Ego, on_delete=models.CASCADE)


class RelPassiveEGO(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    ego = models.ForeignKey(Ego, on_delete=models.CASCADE)
    passive = models.ForeignKey(EgoPassive, on_delete=models.CASCADE)
    is_awakening = models.BooleanField(null=True, blank=True, default=True)


############### Story Text #################


class StoryTheater(models.Model):
    # sub chapter id
    id = models.IntegerField(primary_key=True)
    chapter_id = models.IntegerField()
    unlock_condition = models.JSONField(null=True, blank=True)
    sorting_order = models.IntegerField(null=True, blank=True)
    condition = models.CharField(null=True, blank=True, max_length=20)


class StoryTheaterList(models.Model):
    # StoryId
    id = models.CharField(max_length=30, primary_key=True)
    id_index = models.IntegerField()
    node_id = models.IntegerField()
    # Before or After
    stageDetail = models.CharField(max_length=30, null=True, blank=True)
    story_theater = models.ForeignKey(StoryTheater, on_delete=models.CASCADE)


class EnLimbusStory(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    # like action index
    id_index = models.FloatField()
    id_raw = models.IntegerField()
    theater_story_id = models.ForeignKey(StoryTheaterList, on_delete=models.CASCADE)
    place = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)
    teller = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        indexes = [
            GinIndex(
                fields=["content"], name="content_gin_index", opclasses=["gin_trgm_ops"]
            ),
        ]


class ModelToChar(models.Model):
    #name
    id = models.CharField(max_length=20, primary_key=True)
    krname = models.CharField(max_length=20, blank=True, null=True)
    jpname = models.CharField(max_length=20, blank=True, null=True)
    enname = models.CharField(max_length=20, blank=True, null=True)
    fileName = models.CharField(max_length=50, blank=True, null=True)
    nickName = models.CharField(max_length=50, blank=True, null=True)
    jpNickName = models.CharField(max_length=50, blank=True, null=True)
    enNickName = models.CharField(max_length=50, blank=True, null=True)
    staringSide = models.CharField(max_length=10, blank=True, null=True)
    bottomYPos = models.IntegerField(blank=True, null=True)
    portraitSpritePath = models.CharField(max_length=50, blank=True, null=True)
    nameTagColor = models.CharField(max_length=20, blank=True, null=True)  

    def __str__(self):
        return str(self.enname)
    

import re
class EnStageChapter(models.Model):
    id= models.CharField(max_length=20,primary_key=True)
    company = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    chapter = models.CharField(max_length=50)
    chapterNumber = models.CharField(max_length=10)
    chaptertitle = models.CharField(max_length=100)
    timeline = models.CharField(max_length=20)
    id_int = models.IntegerField()
    def __str__(self):
        return f"{self.chapter} - {self.chaptertitle}"
    

class EnStageNode(models.Model):
    #id is StoryTheaterList node_id
    title = models.CharField(max_length=100, blank=True, null=True)
    place = models.CharField(max_length=100, blank=True, null=True)
    desc = models.TextField(null=True,blank=True)
        
class ENStoryChaptersModel(models.Model):
    title = models.CharField(max_length=100,null=True,blank=True)
    chapterNumber = models.CharField(max_length=100,null=True,blank=True)
    stageDetail = models.CharField(max_length=100,null=True,blank=True)
    chaptertitle = models.CharField(max_length=100,null=True,blank=True)
    chapter = models.CharField(max_length=100,null=True,blank=True)
    node_index = models.IntegerField(null=True,blank=True)
    story_theather_list_node_id = models.IntegerField(null=True,blank=True)

    class Meta:
        managed = False