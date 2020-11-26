from django.test import TestCase
from .factories import NutritionFactory
from .models import Nutrition


class NutritionCoreTestCase(TestCase):
    """ Nutrition Core TestCases """

    def setUp(self):
        # Create Nutrition1 using list_of_nutrition
        self.nutrition1 = NutritionFactory.create(
            typical_value=Nutrition.PER_100G,
            nutrition="fat (10 %), protein (1 g)",
        )

    # TODO Create Nutrition2 using NutritionItemCore

    #
    # Attributes from Abstract Model
    #
    # TODO

    #
    # Attributes from Model
    #
    # TODO

    #
    # Test Model Methods
    #
    def test_representation(self):
        # def __str__(self) is not implemented
        pass

    def test_get_nutrition_items(self):
        self.assertEqual(
            self.nutrition1.get_nutrition_items(), "fat (10 %), protein (1 g)"
        )

    #
    # Miscellaneous
    #
    def test_create_batch(self):
        NutritionFactory.create_batch(499)
        self.assertEquals(Nutrition.objects.count(), 500)  # 499 + setUp one
