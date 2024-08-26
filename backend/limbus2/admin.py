from django.contrib import admin
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
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export import fields, resources, widgets
import json

# Register your models here.

class ArrayFieldWidget(widgets.Widget):
    def clean(self, value, row=None, *args, **kwargs):
        # Handle JSON input specifically
        if isinstance(value, str):
            try:
                # Attempt to parse the string as JSON
                parsed_value = json.loads(value)
                if isinstance(parsed_value, list):
                    return parsed_value
            except json.JSONDecodeError:
                pass
            # Fallback to splitting by comma if not valid JSON
            return value.split(',')
        return value

    def render(self, value, obj=None):
        # Convert the array to a JSON string for export
        return json.dumps(value)


class IdentityResource(resources.ModelResource):
    unitKeyWordList = fields.Field(column_name="unitKeyWordList", attribute="unitKeyWordList",widget=ArrayFieldWidget())
    associationList = fields.Field(column_name="associationList", attribute="associationList",widget=ArrayFieldWidget())
    slotWeightConditionList = fields.Field(column_name="slotWeightConditionList", attribute="slotWeightConditionList",widget=ArrayFieldWidget())
    minSpeedList = fields.Field(column_name="minSpeedList", attribute="minSpeedList",widget=ArrayFieldWidget())
    maxSpeedList = fields.Field(column_name="maxSpeedList", attribute="maxSpeedList",widget=ArrayFieldWidget())
    breakSection = fields.Field(column_name="breakSection", attribute="breakSection",widget=ArrayFieldWidget())

    class Meta:
        model = Identity


class IdentityAdmin(ImportExportModelAdmin):
    resource_class = IdentityResource

admin.site.register(Identity,IdentityAdmin)

class PassiveResource(resources.ModelResource):
    requireIDList = fields.Field(column_name="requireIDList", attribute="requireIDList",widget=ArrayFieldWidget())
    class Meta:
        model = Passive


class PassiveAdmin(ImportExportModelAdmin):
    resource_class = PassiveResource

admin.site.register(Passive,PassiveAdmin)

class AttributionConditionResource(resources.ModelResource):
    class Meta:
        model = AttributeCondition


class AttributeConditionAdmin(ImportExportModelAdmin):
    resource_class = AttributionConditionResource

admin.site.register(AttributeCondition,AttributeConditionAdmin)

class SinnerResource(resources.ModelResource):
    class Meta:
        model = Sinner

class SinnerAdmin(ImportExportModelAdmin):
    resource_class = SinnerResource

admin.site.register(Sinner,SinnerAdmin)

class PanicTypeResource(resources.ModelResource):
    class Meta:
        model = PanicType

class PanicTypeAdmin(ImportExportModelAdmin):
    resource_class = PanicTypeResource
admin.site.register(PanicType,PanicTypeAdmin)

class SkillResource(resources.ModelResource):
    requireIDList = fields.Field(column_name="requireIDList", attribute="requireIDList",widget=ArrayFieldWidget())
    class Meta:
        model = Skill

class SkillAdmin(ImportExportModelAdmin):
    resource_class = SkillResource

admin.site.register(Skill,SkillAdmin)

class SkillEffectResource(resources.ModelResource):
    keywords = fields.Field(column_name="keywords", attribute="keywords",widget=ArrayFieldWidget())
    def save_instance(self, instance, is_create, using_transactions=True, dry_run=False):
        if not instance.skill_id:
            instance.skill_id = Skill.objects.get(id=0).id
        return super().save_instance(instance, is_create, using_transactions, dry_run)
    class Meta:
        model = EnSkillEffect

class SkillEffectAdmin(ImportExportModelAdmin):
    resource_class = SkillEffectResource

admin.site.register(EnSkillEffect,SkillEffectAdmin)

class CoinEffectListResource(resources.ModelResource):
    class Meta:
        model = EnCoinEffectList

class CoinEffectListAdmin(ImportExportModelAdmin):
    resource_class = CoinEffectListResource

admin.site.register(EnCoinEffectList,CoinEffectListAdmin)

class CoinEffectDescResource(resources.ModelResource):
    class Meta:
        model = EnCoinEffectDesc

class CoinEffectDescAdmin(ImportExportModelAdmin):
    resource_class = CoinEffectDescResource

admin.site.register(EnCoinEffectDesc,CoinEffectDescAdmin)


class SkillDataResource(resources.ModelResource):
    class Meta:
        model = SkillData

class SkillDataAdmin(ImportExportModelAdmin):
    resource_class = SkillDataResource

admin.site.register(SkillData,SkillDataAdmin)

class RelPassiveResource(resources.ModelResource):
    class Meta:
        model = RelPassive

class RelPassiveAdmin(ImportExportModelAdmin):
    resource_class = RelPassiveResource
    
admin.site.register(RelPassive,RelPassiveAdmin)


class RelSkillResource(resources.ModelResource):
    class Meta:
        model = RelSkill

class RelSkillAdmin(ImportExportModelAdmin):
    resource_class = RelSkillResource


admin.site.register(RelSkill,RelSkillAdmin)

class ENPassiveDescriptionResource(resources.ModelResource):
    class Meta:
        model = EnPassiveDescription

class ENPassiveDescriptionAdmin(ImportExportModelAdmin):
    resource_class = ENPassiveDescriptionResource


admin.site.register(EnPassiveDescription,ENPassiveDescriptionAdmin)

class CoinListResource(resources.ModelResource):
    class Meta:
        model = CoinList

class CoinListAdmin(ImportExportModelAdmin):
    resource_class = CoinListResource


admin.site.register(CoinList,CoinListAdmin)

class ENIdentityInfoResource(resources.ModelResource):
    class Meta:
        model = EnIdentityInfo

class ENIdentityInfoAdmin(ImportExportModelAdmin):
    resource_class = ENIdentityInfoResource


admin.site.register(EnIdentityInfo,ENIdentityInfoAdmin)

class HPResource(resources.ModelResource):
    class Meta:
        model = Hp

class HPAdmin(ImportExportModelAdmin):
    resource_class = HPResource


admin.site.register(Hp,HPAdmin)

class atkResistListResource(resources.ModelResource):
    class Meta:
        model = AttackResistList

class atkResistListAdmin(ImportExportModelAdmin):
    resource_class = atkResistListResource


admin.site.register(AttackResistList,atkResistListAdmin)


from .models import (
    EgoSkill,
    EgoSkillData,
    EgoCoinList,
    EnEgoSkillEffect,
    EnEgoSkillCoinEffect,
    EnEgoSkillCoinEffectDesc,
    Ego,
    EnEgoInfo,
    EgoAttributeResist,
    EgoRequirement,
    EgoCorrosionSection,
    EgoPassive,
    EnEgoPassive,
    RelPassiveEGO)

for models in [EgoSkill,
    EgoSkillData,
    EgoCoinList,
    EnEgoSkillEffect,
    EnEgoSkillCoinEffect,
    EnEgoSkillCoinEffectDesc,
    Ego,
    EnEgoInfo,
    EgoAttributeResist,
    EgoRequirement,
    EgoCorrosionSection,
    EgoPassive,
    EnEgoPassive,
    RelPassiveEGO]:
    class tempResource(resources.ModelResource):
        class Meta:
            model = models

    class atkResistListAdmin(ImportExportModelAdmin):
        resource_class = tempResource
    admin.site.register(models,atkResistListAdmin)