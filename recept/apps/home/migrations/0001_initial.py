# Generated by Django 4.2.5 on 2024-04-05 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('preparation_steps', models.TextField()),
                ('cooking_time', models.IntegerField()),
                ('image', models.ImageField(upload_to='images/')),
                ('author', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RecipeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.recipe')),
            ],
            options={
                'unique_together': {('recipe', 'category')},
            },
        ),
        migrations.AddField(
            model_name='recipe',
            name='categories',
            field=models.ManyToManyField(through='home.RecipeCategory', to='home.category'),
        ),
    ]
