from django.db import models


class TypicalValueCore(models.Model):
    """
    Typical Value Core
    """

    name = models.CharField(max_length=50, help_text="e.g: per 100ml")

    def __str__(self):
        return self.name


class LabelCore(models.Model):
    """
    Label Core
    """

    name = models.CharField(max_length=50, help_text="e.g: fat, protein, salt")

    def __str__(self):
        return self.name


class NutritionCore(models.Model):
    """
    Nutrition Core model
    """

    list_of_nutrition = models.CharField(
        max_length=1000,
        null=True,
        blank=True,
        help_text="if you don't want to create relations",
    )
    typical_value = models.ForeignKey(
        TypicalValueCore, on_delete=models.CASCADE
    )

    class Meta:
        abstract = True

    def get_nutrition_items(self):
        # Not using the NutritionItemCore
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

    label = models.ForeignKey(LabelCore, on_delete=models.CASCADE)
    amount = models.CharField(max_length=6)
    display_hierarchy = models.IntegerField(default=0)

    class Meta:
        abstract = True
