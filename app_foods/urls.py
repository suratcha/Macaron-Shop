from django.urls import path
from . import views

urlpatterns = [
    path('', views.foods, name = 'foods'),
    path('<int:food_id>', views.food, name = 'food'),
    path('add-to-cart/<int:food_id>/', views.add_to_cart, name='add_to_cart'),
    path('increment/<int:food_id>/', views.increment_cart, name='increment_cart'),
    path('decrement/<int:food_id>/', views.decrement_cart, name='decrement_cart'),
    path('remove-from-cart/<int:food_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.view_cart, name='view_cart'),
]