from .models import (
    Sinner,
    PanicType,
    Passive,
    AttributeCondition,
    EnPassiveDescription,
    Skill,
    EnSkillEffect,
    EnCoinEffectList,
    EnCoinEffectDesc,
    SkillData,
    CoinList,
    Identity,
    EnIdentityInfo,
    Hp,
    AttackResistList,
    RelPassive,
    RelSkill,
    EgoSkill,
    EgoSkillData,
    EgoCoinList,
    EnEgoSkillEffect,
    EnEgoSkillCoinEffect,
    EnEgoSkillCoinEffectDesc,
    EgoPassive,
    EnEgoPassive,
    Ego,
    EnEgoInfo,
    EgoAttributeResist,
    EgoRequirement,
    EgoCorrosionSection,
    RelPassiveEGO,
    StoryTheater,
    StoryTheaterList,
    EnLimbusStory,
    ModelToChar,
)
from .models import (
    Sinner,
    PanicType,
    Passive,
    AttributeCondition,
    EnPassiveDescription,
    Skill,
    EnSkillEffect,
    EnCoinEffectList,
    EnCoinEffectDesc,
    SkillData,
    CoinList,
    Identity,
    EnIdentityInfo,
    Hp,
    AttackResistList,
    RelPassive,
    RelSkill,
    # Possibly missing models like Ego, EgoSkill, etc.
)

modelmap = {
    "0-sinner.json": Sinner,
    "1-PanicType.json": PanicType,
    "2-skill.json": Skill,
    "2.5-skill.json": Skill,
    "2.6-Passive.json": Passive,
    "3-Passive.json": Passive,
    "4-attribution_conditions.json": AttributeCondition,
    "5-EN_Passive_Descriptions.json": EnPassiveDescription,
    "6-skill_data.json": SkillData,
    "7-coin_list.json": CoinList,
    "8-identity.json": Identity,
    "9-identity_HP.json": Hp,
    "10-identity_attkResist.json": AttackResistList,
    "11-identity_skillRelationTable-11.json": RelSkill,
    "12-EN_identity_info.json": EnIdentityInfo,
    "13-EN_skill_effect.json": EnSkillEffect,
    "14-EN_coin_effect_list.json": EnCoinEffectList,
    "15-EN_coin_effect_desc.json": EnCoinEffectDesc,
    "16-rel_passive.json": RelPassive,
    "17-EgoPassive.json": EgoPassive,
    "17.5-EN_EgoPassive.json": EnEgoPassive,
    "24-EgoSkill.json": EgoSkill,
    "25-EgoSkillData.json": EgoSkillData,
    "26-EgoCoinList.json": EgoCoinList,
    "27-EN_EgoSkillEffect.json": EnEgoSkillEffect,
    "28-EN_EgoSkillCoinEffect.json": EnEgoSkillCoinEffect,
    "29-EN_EgoSkillCoinEffectDesc.json": EnEgoSkillCoinEffectDesc,
    "30-ego.json": Ego,
    "31-EgoAttributeResist.json": EgoAttributeResist,
    "32-EgoRequirement.json": EgoRequirement,
    "33-EgoCorrosionSection.json": EgoCorrosionSection,
    "34-RelPassiveEGO.json": RelPassiveEGO,
    "35-EN_EgoInfo.json": EnEgoInfo,
}

foreign_key_map = {
    "4-attribution_conditions.json": {
        "passive": Passive,
    },
    "5-EN_Passive_Descriptions.json": {
        "passive": Passive,
    },
    "6-skill_data.json": {
        "skill": Skill,
    },
    "7-coin_list.json": {
        "skill_data": SkillData,
    },
    "8-identity.json": {
        "characterId": Sinner,
        "panicType": PanicType
    },
    "9-identity_HP.json": {
        "id": Identity
    },
    "10-identity_attkResist.json": {
        "identity": Identity,
    },
    "11-identity_skillRelationTable-11.json": {
        "identity": Identity,
        "skill": Skill
    },
    "12-EN_identity_info.json": {
        "identity": Identity,
    },
    "13-EN_skill_effect.json": {
        "skill": Skill,
    },
    "14-EN_coin_effect_list.json": {
        "skill_coin_effect": EnSkillEffect,
    },
    "15-EN_coin_effect_desc.json": {
        "coin": EnCoinEffectList,
    },
    "16-rel_passive.json": {
        "identity": Identity,
        "passive": Passive
    },
    "17.5-EN_EgoPassive.json": {
        "ego_passive": EgoPassive,
    },
    "25-EgoSkillData.json": {
        "ego_skill": EgoSkill,
    },
    "26-EgoCoinList.json": {
        "ego_skill_data": EgoSkillData,
    },
    "27-EN_EgoSkillEffect.json": {
        "ego_skill": EgoSkill,
    },
    "28-EN_EgoSkillCoinEffect.json": {
        "ego_skill_effect": EnEgoSkillEffect,
    },
    "29-EN_EgoSkillCoinEffectDesc.json": {
        "ego_skill_coin_effect": EnEgoSkillCoinEffect,
    },
    "30-ego.json": {
        "awakeningSkillId": EgoSkill,
        "corrosionSkillId" : EgoSkill,
        "characterId" : Sinner
    },
    "31-EgoAttributeResist.json": {
        "ego": Ego,
    },
    "32-EgoRequirement.json": {
        "ego": Ego,
    },
    "33-EgoCorrosionSection.json": {
        "ego": Ego,
    },
    "34-RelPassiveEGO.json": {
        "ego": Ego,
        "passive": EgoPassive,
    },
    "35-EN_EgoInfo.json": {
        "ego": Ego,
    },
}

import re
def natural_key(file):
    return [
        float(s) if re.fullmatch(r'\d+\.\d+|\d+', s) else s.lower()
        for s in re.split(r'(\d+\.\d+|\d+)', file.name)
    ]