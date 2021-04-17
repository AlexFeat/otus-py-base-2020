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
        Food.objects.create(
            title='Мясная солянка',
            description='Самый мясной суп это наша мясная солянка',
            cost='39',
            category=soup,
            country=rus,
        )

        garnish = Category.objects.create(name='Гарнир')
        # создаём блюда
        Food.objects.create(
            title='Макароны',
            description='Отварные макароны с маслом',
            cost='12',
            category=garnish,
            country=rus,
        )
        Food.objects.create(
            title='Картофельное пюре',
            description='Картофельное пюре на бульоне и молоке',
            cost='15',
            category=garnish,
            country=rus,
        )
        Food.objects.create(
            title='Гручка',
            description='Гречка как гречка',
            cost='10',
            category=garnish,
            country=rus,
        )

        hot_dish = Category.objects.create(name='Горячее')
        # создаём блюда
        Food.objects.create(
            title='Гуляш говяжий',
            description='Тушеное мясо с овощами',
            cost='39.50',
            category=hot_dish,
            country=rus,
        )
        Food.objects.create(
            title='Ёжики',
            description='Тефтели из говяжьего и свинного фарша с рисом и томатной подливой',
            cost='35',
            category=hot_dish,
            country=rus,
        )
        Food.objects.create(
            title='Куриные бифштексы',
            description='Нежно рубленное нежное куриное мясо',
            cost='43',
            category=hot_dish,
            country=rus,
        )

        drink = Category.objects.create(name='Напитки')
        # создаём блюда
        Food.objects.create(
            title='Чай',
            description='Просто чай',
            cost='5',
            category=drink,
            country=rus,
        )
        Food.objects.create(
            title='Кофе',
            description='Обжигающе приятный бразильский кофе',
            cost='14',
            category=drink,
            country=rus,
        )
        Food.objects.create(
            title='Морс',
            description='Леденящий душу облепиховый морс',
            cost='10',
            category=drink,
            country=rus,
        )
