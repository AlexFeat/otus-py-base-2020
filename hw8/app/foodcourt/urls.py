"""foodcourt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import food.views as food
import user.views as user
import order.views as order


urlpatterns = [
    path('admin/', admin.site.urls),
    # main urls
    path('', food.FoodList.as_view(), name='food-list'),
    path('<int:pk>/', food.FoodDetail.as_view(), name='food-get'),
    # user
    path('reg/', user.UserCreateView.as_view(), name='user-reg'),
    path('login/', user.UserLogin.as_view(), name='user-login'),
    path('me/', user.UserView.as_view(), name='user-me'),
    path('logout/', user.UserLogout.as_view(), name='user-logout'),
    # order
    path('order/', order.OrderCreate.as_view(), name='order-add'),
    path('order/my', order.OrderList.as_view(), name='order-list'),
]
