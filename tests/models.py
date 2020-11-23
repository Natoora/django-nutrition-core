from django.db import models
from nutrition_core.models import NutritionCore, NutritionItemCore


class Nutrition(NutritionCore):
    """ Test model that inherit from NutritionCore """

    pass


class NutritionItem(NutritionItemCore):
    nutrition = models.ForeignKey(Nutrition, on_delete=models.CASCADE)
