from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    preparation_steps = models.TextField()
    cooking_time = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, through='RecipeCategory')

    def __str__(self):
        return self.title


class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('recipe', 'category')

    def __str__(self):
        return f'{self.recipe.title} - {self.category.name}'
