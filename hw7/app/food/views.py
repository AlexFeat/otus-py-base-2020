from django.shortcuts import render
from .models import Food


def list(request):
    food = Food.objects.all()
    context = {
        'foods': food,
    }
    return render(request, 'food/index.html', context=context)
