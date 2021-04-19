from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=92, unique=True, blank=False)

    def __str__(self):
        return f'{self.id} ({self.name})'

    def food_count(self):
        return Food.objects.filter(country=self).all().count()


class Category(models.Model):
    name = models.CharField(max_length=92, unique=True, blank=False)

    def __str__(self):
        return f'{self.id} ({self.name})'

    def food_count(self):
        return Food.objects.filter(category=self).all().count()


class Food(models.Model):
    title = models.CharField(max_length=64, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True, default='')
    cost = models.FloatField(null=False, default=0)

    def __str__(self):
        return f'{self.id} ({self.title})'
