from django.db import models
from django.db.models import TextField
from django.utils.translation import gettext_lazy as _
from django_jsonform.models.fields import ArrayField


class NonStrippingTextField(TextField):
    """A TextField that does not strip whitespace at the beginning/end of
    it's value."""

    def formfield(self, **kwargs):
        kwargs['strip'] = False
        return super(NonStrippingTextField, self).formfield(**kwargs)
    


class Sinner(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class BattleKeywords(models.Model):
    in_game_id = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    desc = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Passive(models.Model):
    name = models.CharField(max_length=30)
    desc = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class PassiveEgo(models.Model):
    name = models.CharField(max_length=30)
    desc = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class PassiveAbnormality(models.Model):
    name = models.CharField(max_length=30)
    desc = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class SkillEgo(models.Model):
    name = models.CharField(max_length=30)
    in_game_id = models.CharField(max_length=10)
    level = models.IntegerField()
    AWAKENING = "A"
    CORRISION = "C"

    SKILL_EMOTION_TYPE = [(AWAKENING, "Awakening"), (CORRISION, "Corrision")]
    emotion_type = models.CharField(
        max_length=1, choices=SKILL_EMOTION_TYPE, default=AWAKENING
    )
    character = models.ForeignKey(Sinner,null=True,on_delete=models.SET_NULL)
    desc = models.TextField(null=True, blank=True)
    abName = models.CharField(max_length=30)
    coindescs = NonStrippingTextField(blank=True)
    coin_num = models.IntegerField(null=True, blank=True)
    coin_roll = models.IntegerField(null=True, blank=True)
    coin_mod = models.IntegerField(null=True, blank=True)
    type = models.TextField(null=True, blank=True)
    damage_type = models.CharField(max_length=30, default="Blunt")

    def __str__(self):
        return f"{self.name} {self.level} {self.character} {self.emotion_type}"


class PassiveEnemy(models.Model):
    in_game_id = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    desc = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


# Create your models here.
class Identity(models.Model):
    name = models.CharField(max_length=50, null=True)
    rarity = models.IntegerField()
    sinner = models.ForeignKey(Sinner, null=True, on_delete=models.SET_NULL)
    # in_game_id = models.CharField(max_length=10, null=True, blank=True)
    passive = models.TextField(null=True, blank=True)
    support_passive = models.TextField(null=True, blank=True)
    panic = models.TextField(null=True,blank=True)
    hp = models.IntegerField(default=None, null=True)
    block = models.IntegerField(default=None, null=True)
    FATAL = "F"
    WEAK = "W"
    NORMAL = "N"
    ENDURED = "E"
    INEFFECTIVE = "I"
    IMMUNE = "M"
    RESISTANCE_TYPES = [
        (FATAL, "Fatal"),
        (WEAK, "Weak"),
        (NORMAL, "Normal"),
        (ENDURED, "Endured"),
        (INEFFECTIVE, "Ineffective"),
        (IMMUNE, "Immune"),
    ]
    speed = models.CharField(max_length=10, default=None, null=True)
    defense = models.IntegerField(default=43, null=True)
    # Physical Resistance
    resistance_slash = models.CharField(
        max_length=1, choices=RESISTANCE_TYPES, default=NORMAL
    )
    resistance_pierce = models.CharField(
        max_length=1, choices=RESISTANCE_TYPES, default=NORMAL
    )
    resistance_blunt = models.CharField(
        max_length=1, choices=RESISTANCE_TYPES, default=NORMAL
    )
    image_link = models.CharField(max_length=200, null=True, blank=True, default=None)

    def __str__(self):
        return f"{self.name} ({self.sinner.name})"


class Skill(models.Model):
    class SinTypes(models.TextChoices):
        WRATH = "WR", "Wrath"
        LUST = "LU", "Lust"
        SLOTH = "SL", "Sloth"
        GLUTTONY = "GU", "Gluttony"
        GLOOM = "GL", "Gloom"
        PRIDE = "PR", "Pride"
        ENVY = "EN", "Envy"

    class SkillType(models.TextChoices):
        BLUNT = "BT", "Blunt"
        PIERCE = "PI", "Pierce"
        SLASH = "SL", "Slash"
        BLOCK = "BK", "Block"
        EVADE = "EV", "Evade"
        COUNTER = "CO", "Counter"

    belonged_identity = models.ForeignKey(Identity,related_name="identity",on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=30)
    on_use = models.TextField(blank=True,null=True)
    combat_start = models.TextField(blank=True,null=True)
    coindescs = ArrayField(
            models.CharField(max_length=254,blank=True,null=True),
            size=8,)
    coin_roll = models.IntegerField(null=True, blank=True)
    coin_mod = models.IntegerField(null=True, blank=True)
    coin_num = models.IntegerField(null=True,blank=True)
    skill_type = models.CharField(max_length=2,
                                   choices=SkillType.choices, 
                                   default=SkillType.BLUNT)
    sin_type = models.CharField(max_length=2,
                                   choices=SinTypes.choices, 
                                   default=SinTypes.WRATH)
    weight = models.IntegerField(null=True,blank=True)
    #basically how many skill in the deck
    skill_num = models.IntegerField(null=True,blank = True)

    def __str__(self):
        return f"{self.name}"


class EGO(models.Model):
    name = models.CharField(max_length=50)
    rarity = models.IntegerField()
    in_game_id = models.CharField(max_length=10, null=True, blank=True)
    sinner = models.ForeignKey(
        Sinner, on_delete=models.SET_NULL, null=True, default=None
    )
    is_in_game = models.BooleanField(default=True)
    FATAL = "F"
    WEAK = "W"
    NORMAL = "N"
    ENDURED = "E"
    INEFFECTIVE = "I"
    IMMUNE = "M"

    RESISTANCE_TYPES = [
        (FATAL, "Fatal"),
        (WEAK, "Weak"),
        (NORMAL, "Normal"),
        (ENDURED, "Endured"),
        (INEFFECTIVE, "Ineffective"),
        (IMMUNE, "Immune"),
    ]
    speed = models.CharField(max_length=10, null=True, blank=True)
    resource_used_wrath = models.IntegerField(default=0)
    resource_used_lust = models.IntegerField(default=0)
    resource_used_sloth = models.IntegerField(default=0)
    resource_used_gluttony = models.IntegerField(default=0)
    resource_used_gloom = models.IntegerField(default=0)
    resource_used_pride = models.IntegerField(default=0)
    resource_used_envy = models.IntegerField(default=0)
    awakening_skill = models.ForeignKey(
        SkillEgo,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="awakening_skill",
    )
    corrision_skill = models.ForeignKey(
        SkillEgo,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="corrision_skill",
    )

    passive_on_field = models.ForeignKey(
        PassiveEgo,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="passive_on_field",
    )
    passive_off_field = models.ForeignKey(
        PassiveEgo,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="passive_off_field",
    )
    # # Sin Resistance
    resistance_wrath = models.CharField(
        max_length=1, choices=RESISTANCE_TYPES, default=NORMAL
    )
    resistance_lust = models.CharField(
        max_length=1, choices=RESISTANCE_TYPES, default=NORMAL
    )
    resistance_sloth = models.CharField(
        max_length=1, choices=RESISTANCE_TYPES, default=NORMAL
    )
    resistance_gluttony = models.CharField(
        max_length=1, choices=RESISTANCE_TYPES, default=NORMAL
    )
    resistance_gloom = models.CharField(
        max_length=1, choices=RESISTANCE_TYPES, default=NORMAL
    )
    resistance_pride = models.CharField(
        max_length=1, choices=RESISTANCE_TYPES, default=NORMAL
    )
    resistance_envy = models.CharField(
        max_length=1, choices=RESISTANCE_TYPES, default=NORMAL
    )
    # Physical Resistance
    resistance_slash = models.CharField(
        max_length=1, choices=RESISTANCE_TYPES, default=NORMAL
    )
    resistance_pierce = models.CharField(
        max_length=1, choices=RESISTANCE_TYPES, default=NORMAL
    )
    resistance_blunt = models.CharField(
        max_length=1, choices=RESISTANCE_TYPES, default=NORMAL
    )

    image_link = models.CharField(max_length=200, null=True, blank=True, default=None)

    def __str__(self):
        return f"{self.name } {self.sinner.name}"
