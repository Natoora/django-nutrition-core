# import factory
# import random
# from nutrition_core.models import NutritionCore, TypicalValueCore, LabelCore
#
#
# class TypicalValueFactoryCore(factory.django.DjangoModelFactory):
#     class Meta:
#         model = TypicalValueCore
#
#     typical_value = random.choice(['per 100ml', 'per 100g'])
#
#
# class LabelFactoryCore(factory.django.DjangoModelFactory):
#     class Meta:
#         model = LabelCore
#
#     name = random.choice(['fat', 'protein', 'salt'])
#
#
# class NutritionFactoryCore(factory.django.DjangoModelFactory):
#     class Meta:
#         model = NutritionCore
#
#     typical_value = random(TypicalValueCore.objects.all())
