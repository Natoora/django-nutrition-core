from django.db import models
from django.utils.translation import gettext_lazy as _


class NutritionCore(models.Model):
    """ Nutrition Core model

        Typical Values per 100g/ml

        Energy 1142 kJ / 274 kcal
        Fat                           19 g
        of which Saturates           3.4 g
        Carbohydrate                 0.0 g
        of which Sugars              0.0 g
        Protein                       26 g
        Salt                        13.3 g
    """

    class TypicalValueChoices(models.TextChoices):
        PER_100ML = "PER_100ML", _("Per 100ml")
        PER_100G = "PER_100G", _("Per 100g")

    typical_value = models.CharField(
        max_length=50, choices=TypicalValueChoices.choices
    )
    energy = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        help_text="e.g: 3389 kJ (824 kcal)",
    )
    fat = models.CharField(
        max_length=30, null=False, blank=False, help_text="e.g: 19 g"
    )
    fat_saturates = models.CharField(
        max_length=30, null=False, blank=False, help_text="e.g: 3.4 g"
    )
    carbohydrate = models.CharField(
        max_length=30, null=False, blank=False, help_text="e.g: 0.0 g"
    )
    carbohydrate_sugars = models.CharField(
        max_length=30, null=False, blank=False, help_text="e.g: 0.0 g"
    )
    protein_content = models.CharField(
        max_length=30, null=False, blank=False, help_text="e.g: 26 g"
    )
    salt_content = models.CharField(
        max_length=30, null=False, blank=False, help_text="e.g: 13.3 g"
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.energy  # TODO, improve representation?
