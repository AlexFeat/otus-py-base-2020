from django.views.generic import DetailView, ListView
from .models import Food


class FoodList(ListView):
    model = Food
    template_name = 'food/index.html'


class FoodDetail(DetailView):
    model = Food
    template_name = 'food/detail.html'
