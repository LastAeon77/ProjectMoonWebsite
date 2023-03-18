from django.db import models
from django.contrib.postgres.fields import ArrayField


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
    in_game_id = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    desc = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class PassiveEgo(models.Model):
    in_game_id = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    desc = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class PassiveAbnormality(models.Model):
    in_game_id = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    desc = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=30)
    in_game_id = models.CharField(max_length=10)
    level = models.IntegerField()
    desc = models.TextField(null=True, blank=True)
    coindescs = models.TextField(null=True, blank=True)
    coin_num = models.IntegerField(null=True, blank=True)
    coin_roll = models.IntegerField(null=True, blank=True)
    coin_mod = models.IntegerField(null=True, blank=True)
    type = models.TextField(null=True, blank=True)
    damage_type = models.CharField(max_length=30, default="Blunt")

    def __str__(self):
        return f"{self.name} {self.level} {self.in_game_id}"


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
    desc = models.TextField(null=True, blank=True)
    abName = models.CharField(max_length=30)
    coindescs = models.TextField(null=True, blank=True)
    coin_num = models.IntegerField(null=True, blank=True)
    coin_roll = models.IntegerField(null=True, blank=True)
    coin_mod = models.IntegerField(null=True, blank=True)
    type = models.TextField(null=True, blank=True)
    damage_type = models.CharField(max_length=30, default="Blunt")

    def __str__(self):
        return f"{self.name} {self.level} {self.abName} {self.emotion_type}"


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
    in_game_id = models.CharField(max_length=10, null=True, blank=True)
    passive_on_field = models.ForeignKey(
        Passive,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="passive_on_field",
    )
    passive_off_field = models.ForeignKey(
        Passive,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="passive_off_field",
    )
    growth = models.DecimalField(decimal_places=2, max_digits=6, null=True)
    affinity = models.TextField(null=True, blank=True)
    base_damage = models.DecimalField(decimal_places=2, max_digits=6, null=True)
    skill_1 = models.ForeignKey(
        Skill, null=True, blank=True, on_delete=models.SET_NULL, related_name="skill_1"
    )
    skill_1_count = models.IntegerField(default=3)
    skill_2 = models.ForeignKey(
        Skill, null=True, blank=True, on_delete=models.SET_NULL, related_name="skill_2"
    )
    skill_2_count = models.IntegerField(default=2)
    skill_3 = models.ForeignKey(
        Skill, null=True, blank=True, on_delete=models.SET_NULL, related_name="skill_3"
    )
    skill_3_count = models.IntegerField(default=1)
    is_in_game = models.BooleanField(default=True)
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
    # Sin Resistance
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
        return f"{self.name} ({self.sinner.name})"


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
