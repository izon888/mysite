from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *


# Create your views here.
class HomeNews(ListView):
    model = News
    context_object_name = 'news'
    template_name = 'news/index.html'
    paginate_by = 2

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class HomeCategory(ListView):
    model = News
    context_object_name = 'news'
    template_name = 'news/index.html'
    paginate_by = 2

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True)


class DetailNews(DetailView):
    model = News
    context_object_name = 'news'
    template_name = 'news/news_view.html'

    def get_queryset(self):
        return News.objects.filter(pk=self.kwargs['pk'], is_published=True)


class CreateNews(LoginRequiredMixin, CreateView):
    form_class = FormView
    template_name = 'news/add_news.html'
    context_object_name = 'form'
    login_url = '/admin/'


class Logout_site(View):

    def get(self, request):
        logout(request)
        return redirect('home')


class Login_site(CreateView):
    form_class = LoginForm
    template_name = 'news/login.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username, password)
            user = authenticate(username=username, password=password)
            print(user)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')

        return render(request, self.template_name, {'form': form})


class Register(CreateView):
    form_class = RegForm
    template_name = 'news/create_user.html'
    context_object_name = 'form'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        # get the username and password
        username = self.request.POST['username']
        password = self.request.POST['password1']
        # authenticate user then login
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return redirect('home')


