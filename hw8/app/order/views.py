from django.views.generic import CreateView, ListView
from django.shortcuts import render, redirect
from .models import Order
from .forms import OrderForm
from user.models import User
from food.models import Category, Food


class OrderCreate(CreateView):
    model = Order
    template_name = 'order/create.html'
    success_url = '/'
    form_class = OrderForm

    def get(self, request, *args, **kwargs):
        user = User.get_user_by_session(request)
        if user is None:
            return redirect('user-login')
        context = {
            'categories': []
        }
        for category in Category.objects.all():
            data = {
                'category': category,
                'foods': Food.objects.filter(category=category.id).all()
            }
            context['categories'].append(data)
        return render(request, 'order/create.html', context=context)

    def post(self, request, *args, **kwargs):
        user = User.get_user_by_session(request)
        if user is None:
            return redirect('user-login')
        order = Order(
            count_persons=request.POST.get('persons') or 1,
            address=request.POST.get('address'),
            user=user,
        )
        foods = Food.objects.filter(id__in=request.POST.getlist('food_id')).all()
        order.save()
        for f in foods:
            order.total_cost = order.total_cost + f.cost
            order.food.add(f.id)
        order.save()
        return render(request, 'order/create_done.html', context={'order': order})


class OrderList(ListView):
    model = Order
    template_name = 'order/list.html'
    form_class = OrderForm

    def get(self, request, *args, **kwargs):
        user = User.get_user_by_session(request)
        if user is None:
            return redirect('user-login')
        context = {
            'orders': Order.objects.filter(user=user).prefetch_related('food').order_by('-ts_create').all()
        }
        return render(request, 'order/list.html', context=context)
