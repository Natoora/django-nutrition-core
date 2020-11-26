import factory
from factory.fuzzy import FuzzyChoice
from nutrition_core.models import NutritionCore


class NutritionFactoryCore(factory.django.DjangoModelFactory):
    class Meta:
        model = NutritionCore

    nutrition = factory.Faker("text")
    typical_value = FuzzyChoice(NutritionCore.TYPICAL_VALUE_CHOICES)
