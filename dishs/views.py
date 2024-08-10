from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from app.models import Dish
from app.forms import DishForm

def bluds_list(request):
    if request.user.is_authenticated and request.user.is_superuser:
        # If the user is an administrator, retrieve all objects of the Dish model
        dishes = Dish.objects.all()
        template = 'bluds_list_admin.html'
    else:
        # If the user is not an administrator, retrieve only published objects of the Dish model
        dishes = Dish.objects.filter(published=True)
        template = 'bluds_list.html'

    search_query = request.GET.get('search_query')
    if search_query:
        # Filter dishes based on the search query
        dishes = dishes.filter(name__icontains=search_query)

    context = {'dishes': dishes, 'search_query': search_query}
    return render(request, template, context)

def add_dish(request):
    form = DishForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('bluds_list_admin')

    context = {'form': form}
    return render(request, 'add_dish.html', context)

from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import JsonResponse
def get_user_permissions(user):
    # Ваша логика получения разрешений пользователя
    # Возвращайте объект разрешений, соответствующий пользователю
    # Это может быть экземпляр модели, словарь или другой формат данных,
    # содержащий информацию о разрешениях пользователя
    # Например:
    return {
        'is_admin': user.is_superuser,
        'is_moderator': user.is_staff
    }
def manage_permissions(request):
    users = User.objects.all()
    if request.method == 'POST':
        for user in users:
            permission_key = f'permission_{user.id}'
            if permission_key in request.POST:
                is_admin = request.POST.get(permission_key) == 'admin'
                user.is_superuser = is_admin
                user.save()
        return redirect('manage_permissions')

    permissions = {}
    for user in users:
        permissions[user.id] = {
            'user': user,
            'is_admin': user.is_superuser
        }

    return render(request, 'manage_permissions.html', {'permissions': permissions})

def update_permissions(request):
    user_id = request.POST.get('user_id')
    permission_type = request.POST.get('permission_type')
    is_checked = request.POST.get('is_checked')

    # Perform the logic to update the user's permissions based on the provided data
    # ...

    # Return a JSON response to indicate the success or failure of the update
    return JsonResponse({'success': True})
from app.forms import  IngredientForm
from app.models import Ingredient
def add_ingred(request):
    form = IngredientForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('ingredient_list_admin')

    context = {'form': form}
    return render(request, 'add_ingred.html', context)
from django.shortcuts import render, get_object_or_404, redirect
def delete_ingred(request, ingredient_id):
    ingredients = get_object_or_404(Ingredient, pk=ingredient_id)

    if request.method == 'POST':
        ingredients.delete()
        return redirect('ingredient_list_admin')

    return render(request, 'delete_ingred.html', {'ingredients': ingredients})
from app.forms import OrderForm
from app.models import Order
def edit_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            # выполните дополнительные действия, если необходимо
            return redirect('bluds_list_admin')
    else:
        form = OrderForm(instance=order)

    context = {'form': form}
    return render(request, 'edit_order.html', context)
from django.shortcuts import render, redirect, get_object_or_404
from app.models import Season
from app.forms import SeasonForm
from app.views import clusterize_data
def add_order(request):
    form = OrderForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('bluds_list_admin')

    context = {'form': form}
    return render(request, 'add_order.html', context)
def cluster_view(request):
    clusterize_data()  # Вызываем функцию кластеризации
    dishes = Dish.objects.all()
    ingredients = Ingredient.objects.all()
    context = {
        'dishes': dishes,
        'ingredients': ingredients,
    }
    return render(request, 'clusters.html', context)
from django.shortcuts import render, HttpResponse
from app.models import Dish
from sklearn.cluster import KMeans
# Добавьте другие библиотеки машинного обучения, которые вам понадобятся

def create_virtual_orders(request):
    # Получаем данные о блюдах из базы данных
    dishes = Dish.objects.all()

    # Проверяем, есть ли данные о блюдах
    if not dishes:
        return HttpResponse("No dishes found")  # Или выполните другие действия в случае отсутствия данных
    
    # Преобразуем одномерный массив в двумерный
    dishes_array = [[dish.id] for dish in dishes]
    
    # Пример анализа данных и создания "виртуальных заказов"
    kmeans = KMeans(n_clusters=3)
    kmeans.fit(dishes_array)
    clusters = kmeans.labels_
    
    # Создаем "виртуальные заказы" на основе кластеризации
    virtual_orders = {}



