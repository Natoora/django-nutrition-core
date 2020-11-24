import factory
import random
from nutrition_core.models import NutritionCore, TypicalValueCore, LabelCore


class TypicalValueFactoryCore(factory.django.DjangoModelFactory):
    class Meta:
        model = TypicalValueCore

    name = random.choice(["per 100ml", "per 100g"])


class LabelFactoryCore(factory.django.DjangoModelFactory):
    class Meta:
        model = LabelCore

    name = random.choice(["fat", "protein", "salt"])


class NutritionFactoryCore(factory.django.DjangoModelFactory):
    class Meta:
        model = NutritionCore

    list_of_nutrition = factory.Faker("text")
    typical_value = factory.SubFactory(TypicalValueFactoryCore)
