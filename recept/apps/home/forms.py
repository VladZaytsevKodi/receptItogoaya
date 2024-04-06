from django import forms
from .models import Recipe, Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'preparation_steps', 'cooking_time', 'image', 'categories']
        widgets = {
            'categories': forms.CheckboxSelectMultiple
        }
        labels = {
            'title': 'Название',
            'description': 'Описание',
            'preparation_steps': 'Порядок приготовления',
            'cooking_time': 'Время приготовления',
            'image': 'Изображение',
            'categories': 'Категории'
        }

        def __init__(self, *args, **kwargs):
            user = kwargs.pop('user', None)
            super(RecipeForm, self).__init__(*args, **kwargs)
            if user:
                self.fields['author'] = forms.ModelChoiceField(queryset=user, widget=forms.HiddenInput())


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {
            'name': 'Название',
        }



