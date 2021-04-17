from django.db import models
from django.utils import timezone
from user.models import User
from food.models import Food


class Order(models.Model):
    ts_create = models.DateTimeField(null=False, default=timezone.now)
    total_cost = models.FloatField(null=False, default=0)
    count_persons = models.PositiveSmallIntegerField(default=0, blank=True)
    address = models.TextField(null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ManyToManyField(Food)

    def __str__(self):
        return f'№{self.id} (от {self.ts_create}) для {self.user} на {self.total_cost}'
