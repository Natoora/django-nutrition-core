from django.db import models


class NutritionCore(models.Model):
    """
    Nutrition Core model
    """

    PER_100ML = "PER_100ML"
    PER_100G = "PER_100G"

    TYPICAL_VALUE_CHOICES = ((PER_100ML, "100ml"), (PER_100G, "100g"))

    list_of_nutrition = models.TextField(
        max_length=1000,
        null=True,
        blank=True,
        help_text="if you don't want to create relations",
    )
    typical_value = models.CharField(
        max_length=20, choices=TYPICAL_VALUE_CHOICES, null=False, blank=False
    )

    class Meta:
        abstract = True

    def get_nutrition_items(self):
        # Using the list_of_nutrition
        if self.list_of_nutrition:
            return self.list_of_nutrition

        # Using NutritionItemCore
        long_form = []
        if hasattr(self, "nutritionitem_set"):
            for item in self.nutritionitem_set.all():
                long_form.append(f"{item.label.name} {item.amount}")
                pass
        return ", ".join(long_form)


class NutritionItemCore(models.Model):
    """
    Nutrition Item Core
    """

    SALT = "SALT"
    PROTEIN = "PROTEIN"
    FAT = "FAT"
    FIBRE = "FIBRE"

    LABEL_CHOICES = (
        (SALT, "Salt"),
        (PROTEIN, "Protein"),
        (FAT, "Fat"),
        (FIBRE, "Fibre"),
    )

    label = models.CharField(
        max_length=50, choices=LABEL_CHOICES, null=False, blank=True
    )
    amount = models.CharField(max_length=6)
    display_hierarchy = models.IntegerField(default=0)

    class Meta:
        abstract = True
