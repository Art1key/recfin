from django.contrib import admin
from .models import Dish
from .models import RecipeEquipment
from .models import Order
from .models import Ingredient
from .models import Season
from .models import Type

admin.site.register(Ingredient)
admin.site.register(Order)
admin.site.register(RecipeEquipment)
admin.site.register(Dish)
admin.site.register(Season)
admin.site.register(Type)