from django.views.generic import CreateView, FormView, DetailView
from django.shortcuts import HttpResponseRedirect, HttpResponse, render, redirect
from .models import User
from .forms import UserForm, UserLoginForm
from datetime import datetime as dt


class UserCreateView(CreateView):
    model = User
    template_name = 'user/create.html'
    success_url = '/'
    form_class = UserForm

    def post(self, request, *args, **kwargs):
        user = User.objects.filter(email=request.POST.get('email')).first()
        if user:
            return HttpResponseRedirect('/')
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.auth_token = User._get_session_token()
        return super().form_valid(form)

    def get_form_kwargs(self):
        form_kwargs: dict = super().get_form_kwargs()
        if form_kwargs.get('data'):
            _mutable = form_kwargs['data']._mutable
            form_kwargs['data']._mutable = True
            if form_kwargs['data'].get('password'):
                form_kwargs['data']['password'] = User.salt_password(form_kwargs['data'].get('password'))
            form_kwargs['data']._mutable = _mutable
        return form_kwargs


class UserLogin(FormView):
    model = User
    template_name = 'user/login.html'
    success_url = '/'
    form_class = UserLoginForm

    def get(self, request, *args, **kwargs):
        user = User.get_user_by_session(request)
        if user:
            return redirect('user-me')
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = User.objects.filter(email=request.POST.get('email')).first()
        if user is None:
            return redirect('user-reg')
        if user.password != User.salt_password(request.POST.get('password')):
            return redirect('user-login')
        user.auth_token = User._get_session_token()
        user.auth_expired = User._get_session_expire_time()
        user.save()
        response = HttpResponseRedirect('/')
        response.set_cookie('fcsid', user.auth_token)
        return response


class UserView(DetailView):
    model = User
    template_name = 'user/view.html'

    def get(self, request, *args, **kwargs):
        user = User.get_user_by_session(request)
        if user is None:
            return redirect('user-login')
        response = HttpResponse(render(request, 'user/view.html', context={'user': user}))
        return response


class UserLogout(FormView):
    model = User
    success_url = '/'

    def post(self, request, *args, **kwargs):
        user = User.get_user_by_session(request)
        if user is None:
            return redirect('user-login')
        user.auth_expired = dt.now()
        user.save()
        return redirect('food-list')
