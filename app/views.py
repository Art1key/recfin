from django.shortcuts import render, redirect, HttpResponse
from django.db.models import Q
from .forms import DessertForm
from .models import Dish, Ingredient, Order, RecipeEquipment
from .forms import MeatDishesWithOvenForm
from django.http import HttpResponse
from .forms import IngredientForm

def index(request):
    return render(request, 'index.html') #returns the index.html template
def desserts_without_equipment(request):
    form = DessertForm()
    
    return render(request, 'desserts_without_equipment.html', {'form': form})
def show_dish_details(request):
    if request.method == 'POST':
        form = DessertForm(request.POST)
        if form.is_valid():
            dish_id = form.cleaned_data['name'].id
            try:
                dish = Dish.objects.get(id=dish_id)
                return render(request, 'dish_details.html', {'dish': dish})
            except Dish.DoesNotExist:
                return render(request, 'dish_not_found.html')
    else:
        form = DessertForm()

    return render(request, 'desserts_without_equipment.html', {'form': form})
def meat_dishes_with_oven(request):
    if request.method == 'POST':
        form = MeatDishesWithOvenForm(request.POST)
        if form.is_valid():
            selected_dish = form.cleaned_data['meat_dishes']
            # Действия с выбранным блюдом
    else:
        form = MeatDishesWithOvenForm()
    
    return render(request, 'meat_dishes_with_oven.html', {'form': form})

def dish_list(request):
    dishes = Dish.objects.all()
    return render(request, 'dish_list.html', {'dishes': dishes})
#views.py
from django.shortcuts import render
from .forms import SearchForm
from .models import Dish, Season, Type

def search_dishes(request):
    form = SearchForm(request.POST or None)

    if form.is_valid():
        ingredients = form.cleaned_data.get('ingredients')
        seasons = form.cleaned_data.get('seasons')
        types = form.cleaned_data.get('types')
        equipment = form.cleaned_data.get('equipment')
        queryset = Dish.objects.all()

        if not ingredients or '' in ingredients:
            ingredients = Ingredient.objects.values_list('id', flat=True)

        if not seasons or '' in seasons:
            seasons = Season.objects.all()

        if not types or '' in types:
            types = Type.objects.all()

        if not equipment or '' in equipment:
            equipment = RecipeEquipment.objects.all()

        queryset = queryset.filter(order__name__in=ingredients).distinct()
        queryset = queryset.filter(season__in=seasons)
        queryset = queryset.filter(type__in=types)
        queryset = queryset.filter(equip__in=equipment)

        context = {'form': form, 'dishes': queryset}
        return render(request, 'search_dishes.html', context)

    context = {'form': form}
    return render(request, 'search_dishes.html', context)





from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from .models import Ingredient
from django.shortcuts import render, get_object_or_404, redirect
from .models import Ingredient
from .forms import IngredientForm, DishForm
from django.contrib.admin.views.decorators import staff_member_required

def ingredient_edit(request, ingredient_id):
    ingredient = get_object_or_404(Ingredient, pk=ingredient_id)
    
    if request.method == 'POST':
        form = IngredientForm(request.POST, instance=ingredient)
        if form.is_valid():
            form.save()
            return redirect('ingredient_list_admin')
    else:
        form = IngredientForm(instance=ingredient)
    
    if request.user.is_authenticated and request.user.is_superuser:
        return render(request, 'ingredient_edit_admin.html', {'form': form})
    else:
        return render(request, 'ingredient_list.html', {'form': form})

def ingredient_list(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'ingredient_list.html', {'ingredients': ingredients})

def ingredient_list_admin(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'ingredient_list_admin.html', {'ingredients': ingredients})

def bluds_edit(request, dish_id):
    dish = get_object_or_404(Dish, pk=dish_id)
    
    if request.method == 'POST':
        form = DishForm(request.POST, instance=dish)
        if form.is_valid():
            form.save()
            return redirect('bluds_list_admin')
    else:
        form = DishForm(instance=dish)
    
    if request.user.is_authenticated and request.user.is_superuser:
        return render(request, 'bluds_edit.html', {'form': form})
    else:
        return render(request, 'bluds_list.html', {'form': form})

def bluds_list(request):
    dishes = Dish.objects.all()
    return render(request, 'bluds_list.html', {'dishes': dishes})

def bluds_list_admin(request):
    dishes = Dish.objects.all()
    return render(request, 'bluds_list_admin.html', {'dishes': dishes})

def delete(request, dish_id):
    dishes = get_object_or_404(Dish, pk=dish_id)

    if request.method == 'POST':
        dishes.delete()
        return redirect('bluds_list_admin')

    return render(request, 'delete.html', {'dishes': dishes})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Order

def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        order.delete()
        return redirect('bluds_list_admin')

    context = {'order': order}
    return render(request, 'delete_order.html', context)
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User

class AddUserView(View):
    def get(self, request):
        return render(request, 'add_user.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Создание нового пользователя и сохранение его в базе данных
        user = User.objects.create_user(username=username, password=password)
        
        # Дополнительная логика сохранения пользователя в базу данных
        # ...
        
        return redirect('manage_permissions')  # Замените 'manage_permissions' на ваш URL-шаблон
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.models import User
class DeleteUserView(View):
    def post(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        
        # Обработка удаления пользователя
        user.delete()
        
        return redirect('manage_permissions')


from django.shortcuts import render
from django.http import HttpResponse
from .services import clusterize_data

def index(request):
    # Вызываем функцию кластеризации при загрузке главной страницы
    clusterize_data()
    return HttpResponse("Clustering completed successfully and home page loaded.")
# views.py
from django.shortcuts import render
from .services import clusterize_data

import matplotlib.pyplot as plt
from django.shortcuts import render
from .models import Dish, Order
from .services import clusterize_data

def cluster_view(request):
    # Проведем кластеризацию данных
    clusterize_data()
    
    # Получаем все блюда и заказы из базы данных
    dishes = Dish.objects.all()
    orders = Order.objects.all()
    
    # Создаем списки для хранения данных о кластерах
    cluster_x = []
    cluster_y = []
    cluster_colors = []
    
    # Для каждого блюда добавляем его кластер и данные для визуализации
    for dish in dishes:
        cluster_x.append(dish.calory)
        cluster_y.append(dish.time)
        cluster_colors.append(dish.cluster)
    
    # Для каждого заказа также добавляем его кластер и данные для визуализации
    for order in orders:
        # Используем связанные объекты для получения данных о блюде
        cluster_x.append(order.recipe.calory)
        cluster_y.append(order.recipe.time)
        cluster_colors.append(order.cluster)
    
    # Создаем scatter plot для визуализации кластеризации
    plt.figure(figsize=(10, 6))
    plt.scatter(cluster_x, cluster_y, c=cluster_colors, cmap='viridis', marker='o', alpha=0.8)
    plt.xlabel('Calories')
    plt.ylabel('Time')
    plt.title('Cluster Visualization')
    plt.colorbar(label='Cluster')
    
    # Сохраняем график в виде изображения
    image_path = 'cluster_visualization.png'
    plt.savefig(image_path)
    
    # Передаем путь к изображению в контекст шаблона для отображения на веб-странице
    context = {'image_path': image_path}
    
    # Возвращаем шаблон и контекст
    return render(request, 'cluster_view.html', context)
# views.py
from django.shortcuts import render, redirect
from .forms import OrderForm

def home(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Или другой URL после успешного сохранения
    else:
        form = OrderForm()
    return render(request, 'home.html', {'form': form})
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from .models import Dish, Selected
from decimal import Decimal
def create_order_view(request):
    if request.method == 'POST':
        selected_dishes_ids = request.POST.getlist('dishes')
        num_persons = request.POST.get('num_persons')
        total_cost = Decimal('0')  # Инициализируем total_cost перед использованием
        
        for dish_id in selected_dishes_ids:
            dish = Dish.objects.get(pk=dish_id)
            quantity = int(request.POST.get('quantity_{}'.format(dish_id)))  # Получаем количество для каждого блюда
            total_cost += dish.price_dish * quantity * int(num_persons)  # Увеличиваем total_cost

            # Создаем объект Selected для каждого блюда
            selected_item = Selected.objects.create(
                dish=dish,
                quantity=quantity,
                num_persons=num_persons,
                total_cost=dish.price_dish * quantity * int(num_persons)
            )

        return redirect('home')
    else:
        dishes = Dish.objects.all()
        return render(request, 'create_order.html', {'dishes': dishes})
# views.py

# views.py

# views.py

from django.shortcuts import render
from django.db.models import Count
from django.utils import timezone
from django.db.models.functions import ExtractWeekDay
from .models import Selected, Order
import random  # Для генерации случайного числа

def display_graphs(request):
    # Getting the current date and time
    today = timezone.localdate()
    current_hour = timezone.localtime().hour

    # Getting the real number of orders for today
    real_orders_today = Selected.objects.filter(
        created_at__date=today
    ).count()

    # Getting the most ordered dishes in the current day
    most_ordered_dishes = Selected.objects.filter(
        created_at__date=today
    ).values('dish__name').annotate(total=Count('id')).order_by('-total')[:5]

    # Getting the most ordered dish at the current hour
    most_ordered_dish_current_time = Selected.objects.filter(
        created_at__hour=current_hour
    ).values('dish__name').annotate(total=Count('id')).order_by('-total').first()

    # Getting the top 3 most used ingredients in the current day
    top_ingredients = Order.objects.filter(
        recipe__selected__created_at__date=today
    ).values('name__name').annotate(total=Count('id')).order_by('-total')[:3]

    # Forecasting the number of orders for today
    forecasted_orders_today = round(real_orders_today * 1.5)  # Multiply by 1.5 and round to the nearest integer

    # Getting the number of orders per day of the week
    orders_per_day = Selected.objects.filter(
        created_at__date__week_day=ExtractWeekDay('created_at')
    ).annotate(day_of_week=ExtractWeekDay('created_at')).values('day_of_week').annotate(total=Count('id')).order_by('day_of_week')

    # Days of the week labels for plotting
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Extracting the order counts and aligning them by day of the week
    order_counts = [0] * 7
    for order in orders_per_day:
        order_counts[order['day_of_week'] - 1] = order['total']

    # Plotting
    plt.figure(figsize=(8, 6))
    plt.bar(days_of_week, order_counts)
    plt.xlabel('Day of the Week')
    plt.ylabel('Number of Orders')
    plt.title('Number of Orders per Day of the Week')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Saving the plot to a file
    plot_path = 'plot.png'
    plt.savefig(plot_path)
    plt.close()  # Close the plot to avoid overlapping

    context = {
        'most_ordered_dishes': most_ordered_dishes,
        'most_ordered_dish_current_time': most_ordered_dish_current_time,
        'top_ingredients': top_ingredients,
        'real_orders_today': real_orders_today,
        'forecasted_orders_today': forecasted_orders_today,
        'plot_path': plot_path,
    }

    return render(request, 'display_graphs.html', context)











