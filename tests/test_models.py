from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError
from django.test import TestCase
from .factories import NutritionFactory
from .models import Nutrition
import string
import random


class CustomerCoreTestCase(TestCase):
    """ Customer Core TestCases """

    def setUp(self):
        self.nutrition = NutritionFactory.create(
            energy="3389 kJ (824 kcal)",
            fat="19 g",
            fat_saturates="3.4 g",
            carbohydrate="0.0 g",
            carbohydrate_sugars="0.0 g",
            protein_content="26 g",
            salt_content="13.3 g",
        )

    #
    # Attributes from Abstract Model
    #

    # energy TODO ALL possible cases
    def test_energy(self):
        self.assertEqual(self.nutrition.energy, "3389 kJ (824 kcal)")

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

    #
    # Miscellaneous
    #
    def test_create_batch(self):
        NutritionFactory.create_batch(499)
        self.assertEquals(Nutrition.objects.count(), 500)  # 499 + setUp one
