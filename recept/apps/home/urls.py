from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/', views.category, name='category'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/add/', views.recipe_add, name='recipe_add'),
    path('recipe/edit/<int:recipe_id>/', views.recipe_edit, name='recipe_edit'),
    path('category/add/', views.category_add, name='category_add'),
    path('login/', views.loginp, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.signup_page, name='signup'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_signup/', views.signup, name='user_signup'),
]