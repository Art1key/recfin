from django import forms
from .models import Dish, RecipeEquipment, Type, Order

class DessertForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(DessertForm, self).__init__(*args, **kwargs)
        
        self.fields['name'] = forms.ModelChoiceField(
            queryset=Dish.objects.filter(type__name='Десерт', equip__name='Не требуется'),
            label='Dessert Name'
        )
class MeatDishesWithOvenForm(forms.Form):
    meat_dishes = forms.ModelChoiceField(
        queryset=Dish.objects.filter(order__name__name__icontains='Мясо', equip__name='Духовка').distinct(),
        label='Meat Dishes'
    )

# forms.py
from django import forms
from .models import Ingredient, Season, Type, RecipeEquipment

from django import forms
from .models import Ingredient, Season, Type, RecipeEquipment

class SearchForm(forms.Form):
    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all().order_by('name'),
        widget=forms.SelectMultiple(attrs={'class': 'form-control', 'multiple': 'multiple'}),
        required=False
    )

    seasons = forms.ModelMultipleChoiceField(
        queryset=Season.objects.all().order_by('name'),
        widget=forms.SelectMultiple(attrs={'class': 'form-control', 'multiple': 'multiple'}),
        required=False
    )

    types = forms.ModelMultipleChoiceField(
        queryset=Type.objects.all().order_by('name'),
        widget=forms.SelectMultiple(attrs={'class': 'form-control', 'multiple': 'multiple'}),
        required=False
    )

    equipment = forms.ModelMultipleChoiceField(
        queryset=RecipeEquipment.objects.all().order_by('name'),
        widget=forms.SelectMultiple(attrs={'class': 'form-control', 'multiple': 'multiple'}),
        required=False
    )

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['ingredients'].queryset = self.fields['ingredients'].queryset | Ingredient.objects.none()
        self.fields['seasons'].queryset = self.fields['seasons'].queryset | Season.objects.none()
        self.fields['types'].queryset = self.fields['types'].queryset | Type.objects.none()
        self.fields['equipment'].queryset = self.fields['equipment'].queryset | RecipeEquipment.objects.none()

        self.fields['ingredients'].choices = [('', 'Любой')] + list(self.fields['ingredients'].choices)
        self.fields['seasons'].choices = [('', 'Любой')] + list(self.fields['seasons'].choices)
        self.fields['types'].choices = [('', 'Любой')] + list(self.fields['types'].choices)
        self.fields['equipment'].choices = [('', 'Любой')] + list(self.fields['equipment'].choices)

    def clean(self):
        cleaned_data = super().clean()
        ingredients = cleaned_data.get('ingredients')
        seasons = cleaned_data.get('seasons')
        types = cleaned_data.get('types')
        equipment = cleaned_data.get('equipment')

        if ingredients and ingredients[0] == '':
            cleaned_data['ingredients'] = Ingredient.objects.all()

        if seasons and seasons[0] == '':
            cleaned_data['seasons'] = Season.objects.all()

        if types and types[0] == '':
            cleaned_data['types'] = Type.objects.all()

        if equipment and equipment[0] == '':
            cleaned_data['equipment'] = RecipeEquipment.objects.all()

        return cleaned_data








from django import forms
from .models import Ingredient

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'unit']

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'unit']

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'weight', 'calory', 'time', 'timehours', 'price_dish', 'type', 'season', 'equip']
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'amount', 'price', 'recipe', 'order']
from .models import Season

class SeasonForm(forms.ModelForm):
    class Meta:
        model = Season
        fields = ['name']
from django import forms
from .models import Dish, Selected

class OrderDish(forms.ModelForm):
    quantity = forms.IntegerField(min_value=1)
    num_persons = forms.IntegerField(min_value=1)
    dishes = forms.ModelMultipleChoiceField(queryset=Dish.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Selected
        fields = ['dishes', 'quantity', 'num_persons']



