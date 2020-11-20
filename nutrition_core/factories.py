import factory
from factory.fuzzy import FuzzyChoice
from nutrition_core.models import NutritionCore


class NutritionFactoryCore(factory.django.DjangoModelFactory):
    class Meta:
        model = NutritionCore

    typical_value = FuzzyChoice(NutritionCore.TypicalValueChoices)

    # TODO, make it random using FB
    energy = "3389 kJ (824 kcal)"
    fat = "19 g"
    fat_saturates = "3.4 g"
    carbohydrate = "0.0 g"
    carbohydrate_sugars = "0.0 g"
    protein_content = "26 g"
    salt_content = "13.3 g"
