from tests.models import Nutrition
from nutrition_core.factories import NutritionFactoryCore


class NutritionFactory(NutritionFactoryCore):
    class Meta:
        model = Nutrition
