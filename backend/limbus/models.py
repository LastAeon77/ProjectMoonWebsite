from django.db import models


class Sinner(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Create your models here.
class Identity(models.Model):
    name = models.CharField(max_length=50, null=True)
    rarity = models.IntegerField()
    sinner = models.ForeignKey(Sinner, on_delete=models.CASCADE)
    passive_on_field = models.TextField(null=True, blank=True)
    passive_off_field = models.TextField(null=True, blank=True)
    skills = models.TextField()
    FATAL = "F"
    WEAK = "W"
    NORMAL = "N"
    ENDURED = "E"
    INEFFECTIVE = "I"
    RESISTANCE_TYPES = [
        (FATAL, "Fatal"),
        (WEAK, "Weak"),
        (NORMAL, "Normal"),
        (ENDURED, "Endured"),
        (INEFFECTIVE, "Ineffective"),
    ]
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

    def __str__(self):
        return self.name


class EGO(models.Model):
    name = models.CharField(max_length=50)
    rarity = models.IntegerField()
    FATAL = "F"
    WEAK = "W"
    NORMAL = "N"
    ENDURED = "E"
    INEFFECTIVE = "I"
    RESISTANCE_TYPES = [
        (FATAL, "Fatal"),
        (WEAK, "Weak"),
        (NORMAL, "Normal"),
        (ENDURED, "Endured"),
        (INEFFECTIVE, "Ineffective"),
    ]
    resource_used_wrath = models.IntegerField(default=0)
    resource_used_lust = models.IntegerField(default=0)
    resource_used_sloth = models.IntegerField(default=0)
    resource_used_gluttony = models.IntegerField(default=0)
    resource_used_gloom = models.IntegerField(default=0)
    resource_used_pride = models.IntegerField(default=0)
    resource_used_envy = models.IntegerField(default=0)
    skills = models.TextField()

    passive_on_field = models.TextField(null=True, blank=True)
    passive_off_field = models.TextField(null=True, blank=True, default=None)
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

    def __str__(self):
        return self.name
