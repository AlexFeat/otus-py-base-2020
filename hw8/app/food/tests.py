from django.test import TestCase
from .models import Food, Category, Country


class TestFood(TestCase):

    def setUp(self):
        self.country = Country.objects.create(name='Италия')
        self.category1 = Category.objects.create(name='Суп')

    def test_count_empty_for_country(self):
        self.assertEqual(self.country.food_count(), 0)

    def test_count_empty_for_category(self):
        self.assertEqual(self.category1.food_count(), 0)

    def test_count(self):
        Food.objects.create(
            title='Аквакотта',
            description='Традиционный суп территории Мареммы (Maremma). Изначально он считался крестьянской пищей. '
                        'Его рецепт был изобретён для применения зачерствевшего хлеба.',
            cost=53.25,
            country=self.country,
            category=self.category1,
        )
        self.assertEqual(self.country.food_count(), 1)
        self.assertEqual(self.category1.food_count(), 1)
