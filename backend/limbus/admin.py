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
)
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(Sinner)
admin.site.register(Identity)
admin.site.register(EGO)

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
# Skill
class SkillResource(resources.ModelResource):
    class Meta:
        model = Skill


class SkillAdmin(ImportExportModelAdmin):
    resource_class = SkillResource


admin.site.register(Skill, SkillAdmin)
# SkillEGO
class SkillEgoResource(resources.ModelResource):
    class Meta:
        model = SkillEgo


class SkillEgoAdmin(ImportExportModelAdmin):
    resource_class = SkillEgoResource


admin.site.register(SkillEgo, SkillEgoAdmin)
