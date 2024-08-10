from django.db import models
from django.utils import timezone
from django import forms

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Order(models.Model):
    name = models.ForeignKey('Ingredient', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    recipe = models.ForeignKey('Dish', on_delete=models.CASCADE)
    order = models.BigIntegerField()

    def __str__(self):
        return str(self.name)
    
class Dish(models.Model):
    name = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    calory = models.FloatField()
    time = models.DecimalField(max_digits=10, decimal_places=2)
    timehours = models.TextField()
    price_dish = models.BigIntegerField()
    type = models.ForeignKey('Type', on_delete=models.CASCADE)
    season = models.ForeignKey('Season', on_delete=models.CASCADE)
    equip = models.ForeignKey('RecipeEquipment', on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
class RecipeEquipment(models.Model):
    name = models.CharField(max_length=100)
    price_eq = models.BigIntegerField()
    
    def __str__(self):
        return self.name
    
class Season(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Type(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Selected(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    num_persons = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    def __str__(self):
        return f"{self.dish.name} - {self.created_at}"
class Meta:
    verbose_name_plural= "Entries"