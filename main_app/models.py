from django.db import models
from django.contrib.auth.models import User

class Food(models.Model):

    name = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    notes = models.TextField(max_length=500)
    favorite_food = models.BooleanField(default=False)
    budget_item = models.BooleanField(default=False)
    pantry_staple = models.BooleanField(default=False)
    kid_approved = models.BooleanField(default=False)
    picky_approved = models.BooleanField(default=False)
    eat_alone = models.BooleanField(default=False)
    sick_friendly = models.BooleanField(default=False)
    low_spoons = models.BooleanField(default=False)
    texture_friendly  = models.BooleanField(default=False)
    color_friendly  = models.BooleanField(default=False)
    arfid_approved  = models.BooleanField(default=False)
    diet_friendly  = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Recipe(models.Model):

    name = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    directions = models.TextField(max_length=500)
    favorite_recipe = models.BooleanField(default=False)
    budget_meal = models.BooleanField(default=False)
    staple_meal = models.BooleanField(default=False)
    kid_approved = models.BooleanField(default=False)
    picky_approved = models.BooleanField(default=False)
    easy_prep = models.BooleanField(default=False)
    sick_friendly = models.BooleanField(default=False)
    low_spoons = models.BooleanField(default=False)
    texture_friendly  = models.BooleanField(default=False)
    color_friendly  = models.BooleanField(default=False)
    arfid_approved  = models.BooleanField(default=False)
    diet_friendly  = models.BooleanField(default=False)
    foods = models.ManyToManyField(Food)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Cookbook(models.Model):

    name = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    recipes = models.ManyToManyField(Recipe)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']