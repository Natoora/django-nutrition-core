from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError
from django.test import TestCase

# from .factories import NutritionFactory
from .models import Nutrition, NutritionItem
import string
import random
from nutrition_core.models import TypicalValueCore, LabelCore


class NutritionCoreTestCase(TestCase):
    """ Nutrition Core TestCases """

    def setUp(self):

        # NutritionFactory.create(typical_value_core=TypicalValueCore.objects.first())

        self.typical_value = TypicalValueCore()
        self.typical_value.name = "per 100ml"
        self.typical_value.save()

        self.label_fat = LabelCore()
        self.label_fat.name = "fat"
        self.label_fat.save()

        self.label_protein = LabelCore()
        self.label_protein.name = "protein"
        self.label_protein.save()

        self.nutrition = Nutrition()
        self.nutrition.typical_value = self.typical_value
        self.nutrition.save()

        self.nutrition_item_fat = NutritionItem()
        self.nutrition_item_fat.nutrition = self.nutrition
        self.nutrition_item_fat.label = self.label_fat
        self.nutrition_item_fat.amount = "(10 %)"
        self.nutrition_item_fat.save()

        self.nutrition_item_protein = NutritionItem()
        self.nutrition_item_protein.nutrition = self.nutrition
        self.nutrition_item_protein.label = self.label_protein
        self.nutrition_item_protein.amount = "(1 g)"
        self.nutrition_item_protein.save()

        # self.nutrition = NutritionFactory.create(
        #     # energy="3389 kJ (824 kcal)",
        #     # fat="19 g",
        #     # fat_saturates="3.4 g",
        #     # carbohydrate="0.0 g",
        #     # carbohydrate_sugars="0.0 g",
        #     # protein_content="26 g",
        #     # salt_content="13.3 g",
        # )

    #
    # Attributes from Abstract Model
    #

    # energy TODO ALL possible cases
    def test_typical_value(self):
        self.assertEqual(self.nutrition.typical_value.name, "per 100ml")

    # fat

    # fat_saturates

    # carbohydrate

    # carbohydrate_sugars

    # protein_content

    # salt_content

    #
    # Attributes from Model
    #

    #
    # Test Model Methods
    #
    # def test_representation(self):
    #     self.assertEqual(self.customer.__str__(), self.customer.name)
    def test_get_nutrition_items(self):
        self.assertEqual(
            self.nutrition.get_nutrition_items(), "fat (10 %), protein (1 g)"
        )

    #
    # Miscellaneous
    #
    # def test_create_batch(self):
    #     NutritionFactory.create_batch(499)
    #     self.assertEquals(Nutrition.objects.count(), 500)  # 499 + setUp one
