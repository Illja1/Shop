from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm,UserLoginForm
from django.contrib.auth import login, logout
from django.contrib import messages
from .models import Item, Category
from django.core.paginator import Paginator
from django.db.models import Count
from django.views.decorators.cache import cache_page

def index(request):
    object = Item.objects.get_queryset().select_related('category').order_by('id')
    price = Item.objects.all()
    categories = Category.objects.all()
    p = Paginator(object, 5)
    page = request.GET.get('page',1 )
    objects_list = p.get_page(page)
    context = {
    'categories': categories,
    'objects_list':objects_list,
    'object':object
    }
    return render(request, 'polls/landing.html',context=context)

def user_logout(request):
    logout(request)
    return redirect('index')

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Register complete')
            return redirect('login')
        else:
            messages.error(request, 'Register not complete')
    else:
            form = UserRegisterForm()
    return render(request, 'polls/register.html',{"form":form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('index')
    else:
            form = UserLoginForm()
    return render(request, 'polls/login.html',{"form":form})


def get_category(request,category_id):
    object = Item.objects.select_related('category').filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    p = Paginator(object, 5)
    page = request.GET.get('page',1 )
    objects_list = p.get_page(page)
    context = {
    'object':object,
    'categories': categories,
    'category':category,
    'objects_list':objects_list,
    'title':'Катерогії',
    }

    return render(request,'polls/category.html',context=context)
