from django.contrib import admin
from .models import (
    Sinner,
    Identity,
    EGO,
    Passive,
    PassiveAbnormality,
    PassiveEgo,
    PassiveEnemy,
    Skill,
    SkillEgo,
    BattleKeywords,
    Faction
)
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(Sinner)
# Identity
class IdentityResource(resources.ModelResource):
    class Meta:
        model = Identity


class IdentityAdmin(ImportExportModelAdmin):
    resource_class = IdentityResource


admin.site.register(Identity, IdentityAdmin)

# Faction
admin.site.register(Faction)

# Ego
class EGOResource(resources.ModelResource):
    class Meta:
        model = EGO


class EGOAdmin(ImportExportModelAdmin):
    resource_class = EGOResource


admin.site.register(EGO, EGOAdmin)
# admin.site.register(EGO)
# Passive
class PassiveResource(resources.ModelResource):
    class Meta:
        model = Passive


class PassiveAdmin(ImportExportModelAdmin):
    resource_class = PassiveResource


admin.site.register(Passive, PassiveAdmin)
# Passive Abnormality
class PassiveAbnormalityResource(resources.ModelResource):
    class Meta:
        model = PassiveAbnormality


class PassiveAbnormalityAdmin(ImportExportModelAdmin):
    resource_class = PassiveAbnormalityResource


admin.site.register(PassiveAbnormality, PassiveAbnormalityAdmin)

# Passive EGO
class PassiveEgoResource(resources.ModelResource):
    class Meta:
        model = PassiveEgo


class PassiveEgoAdmin(ImportExportModelAdmin):
    resource_class = PassiveEgoResource


admin.site.register(PassiveEgo, PassiveEgoAdmin)
admin.site.register(Skill)
# SkillEGO
class SkillEgoResource(resources.ModelResource):
    class Meta:
        model = SkillEgo


class SkillEgoAdmin(ImportExportModelAdmin):
    resource_class = SkillEgoResource


admin.site.register(SkillEgo, SkillEgoAdmin)

# BattleKeywords


class BattleKeywordsResource(resources.ModelResource):
    class Meta:
        model = BattleKeywords


class BattleKeywordsAdmin(ImportExportModelAdmin):
    resource_class = BattleKeywordsResource


admin.site.register(BattleKeywords, BattleKeywordsAdmin)
