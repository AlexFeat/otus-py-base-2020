from django.core.management.base import BaseCommand
from food.models import Category, Country, Food


class Command(BaseCommand):
    def handle(self, *args, **options):
        # очистка БД
        Food.objects.all().delete()
        Category.objects.all().delete()
        Country.objects.all().delete()

        # создаём справочники
        soup = Category.objects.create(name='Супы')
        rus = Country.objects.create(name='Россия')

        # создаём блюда
        Food.objects.create(
            title='Борщ',
            description='Горячий свекольный суп с мясом',
            cost='35',
            category=soup,
            country=rus,
        )
        Food.objects.create(
            title='Окрошка на квасе',
            description='Холодный суп на квасе',
            cost='24',
            category=soup,
            country=rus,
        )
        Food.objects.create(
            title='Окрошка на кефире',
            description='Холодный овощной суп с мясом на кефире',
            cost='19',
            category=soup,
            country=rus,
        )
