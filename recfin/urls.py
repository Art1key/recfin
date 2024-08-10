"""
URL configuration for recfin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import desserts_without_equipment
from app.views import show_dish_details
from app.views import dish_list
from app.views import meat_dishes_with_oven
from accounts import views
from app.views import ingredient_list
from app.views import search_dishes, AddUserView, DeleteUserView
from accounts.views import logout_view
from app.views import ingredient_list_admin,ingredient_edit, cluster_view, bluds_list, bluds_list_admin, bluds_edit, delete, delete_order, create_order_view, display_graphs
from dishs.views import add_dish, manage_permissions, update_permissions, add_ingred, delete_ingred, edit_order,add_order, create_virtual_orders
app_name = 'dishs' 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('desserts-without-equipment/', desserts_without_equipment, name='desserts_without_equipment'),
    path('show_dish_details/', show_dish_details, name='show_dish_details'),
    path('meat_dishes_with_oven/', meat_dishes_with_oven, name='meat_dishes_with_oven'),
    path('dish_list/',dish_list, name='dish_list'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('bluds/list', bluds_list, name='bluds_list'),
    path('bluds/list/admin', bluds_list_admin, name='bluds_list_admin'),
    path('bluds/<int:dish_id>/edit/', bluds_edit, name='bluds_edit'),
    path('dish/<int:dish_id>/delete/', delete, name='delete'),
    path('search_dishes/', search_dishes, name='search_dishes'),
    path('ingredient/list/', ingredient_list, name='ingredient_list'),
    path('ingredient/list/admin', ingredient_list_admin, name='ingredient_list_admin'),
    path('ingredient/<int:ingredient_id>/edit/', ingredient_edit, name='ingredient_edit'),
    path('add_dish/', add_dish, name='add_dish'),
    path('manage-permissions/', manage_permissions, name='manage_permissions'),
    path('update-permissions/', update_permissions, name='update_permissions'),
    path('add_ingred/', add_ingred, name='add_ingred'),
    path('ingredient/<int:ingredient_id>/delete_ingred/', delete_ingred, name='delete_ingred'),
    path('add_order/', add_order, name='add_order'),
    path('edit_order/<int:order_id>/', edit_order, name='edit_order'),
    path('orders/<int:order_id>/delete/', delete_order, name='delete_order'),
    path('user/add/', AddUserView.as_view(), name='add_user'),
    path('delete-user/<int:user_id>/', DeleteUserView.as_view(), name='delete_user'),
    path('cluster/', cluster_view, name='cluster_view'), 
    path('create_virtual_orders/', create_virtual_orders, name='create_virtual_orders'),
    path('create_order/', create_order_view, name='create_order'),
    path('display_graphs/', display_graphs, name='display_graphs'),
]
