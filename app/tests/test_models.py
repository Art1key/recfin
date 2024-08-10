from django.test import TestCase
from decimal import Decimal
from app.models import Ingredient, Order, Dish, RecipeEquipment, Season, Type

class IngredientModelTest(TestCase):

    def test_str_representation(self):
        ingredient = Ingredient(name='Сардины', unit='кг')
        self.assertEqual(str(ingredient), 'Сардины')
class DishModelTest(TestCase):

    def test_str_representation(self):
        dish = Dish(name='Сардины под шубой', weight=500, calory=300, time=30, timehours='30 минут', price_dish=200)
        self.assertEqual(str(dish), 'Сардины под шубой')

class RecipeEquipmentModelTest(TestCase):

    def test_str_representation(self):
        equipment = RecipeEquipment()
        self.assertEqual(str(equipment), 'Блендер')

class SeasonModelTest(TestCase):

    def test_str_representation(self):
        season = Season(name='Зима')
        self.assertEqual(str(season), 'Зима')

class TypeModelTest(TestCase):

    def test_str_representation(self):
        dish_type = Type(name='Рыбный салат')
        self.assertEqual(str(dish_type), 'Рыбный салат')
