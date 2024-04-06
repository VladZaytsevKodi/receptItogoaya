from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

# Create your views here.
from django.shortcuts import render, redirect
from .models import Recipe, Category

from .forms import RecipeForm, CategoryForm


def index(request):
    recipes = Recipe.objects.all().order_by('?')[:5]
    return render(request, 'home/index.html', {'recipes': recipes})


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'home/recipe.html', {'recipe': recipe})


def recipe_add(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            form.save_m2m()  #
            return redirect('recipe_detail', recipe_id=recipe.id)
    else:
        form = RecipeForm()
    return render(request, 'home/add_recipe.html', {'form': form})


def recipe_edit(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'home/edit_recipe.html', {'form': form})


def category_add(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipe_add')
    else:
        form = CategoryForm()
    return render(request, 'home/category_add.html', {'form': form})


def category(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})


def loginp(request):
    return render(request, 'home/login.html', )


def signup_page(request):
    return render(request, 'home/signup.html', )


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        mail = request.POST['mail']
        pwd = request.POST['pwd']
        new_user = User.objects.create_user(username, mail, pwd)
        new_user.first_name = first_name
        new_user.last_name = last_name
        new_user.save()
        messages.success(request, 'Account has been created successfully.')
    return redirect('login')


def user_login(request):
    if not request.user.is_authenticated:

        if request.method == 'POST':
            uname = request.POST['uname']
            pwd = request.POST['pwd']

            check_user = authenticate(username=uname, password=pwd)
            if check_user is not None:
                login(request, check_user)
                return redirect('login')
            else:
                messages.warning(request, 'Invalid Username or Password.')
                return redirect('login')
        return redirect('index')

    else:
        return redirect('index')


def user_logout(request):
    logout(request)
    return redirect('index')
