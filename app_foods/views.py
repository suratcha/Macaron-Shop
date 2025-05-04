from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Food, Order, OrderItem

# Create your views here.
def foods(request):
    all_foods = Food.objects.order_by('-recommend')
    context = { 'foods' : all_foods }
    return render(request, 'app_foods/foods.html', context)

def food(request, food_id):
    one_food = None 
    try:
        one_food = Food.objects.get(id=food_id)
    except:
        print('No')
    context = { 'food': one_food }
    return render(request, 'app_foods/food.html', context)

def add_to_cart(request, food_id):
    cart = request.session.get('cart', {})
    if request.method == 'POST':
        try:
            quantity = int(request.POST.get('quantity', 1))
            if quantity < 1:
                quantity = 1
        except (ValueError, TypeError):
            quantity = 1
    else:
        quantity = 1

    cart[str(food_id)] = cart.get(str(food_id), 0) + quantity
    request.session['cart'] = cart
    return redirect('food', food_id=food_id)

def increment_cart(request, food_id):
    cart = request.session.get('cart', {})
    cart[str(food_id)] = cart.get(str(food_id), 0) + 1
    request.session['cart'] = cart
    return redirect('view_cart')

def decrement_cart(request, food_id):
    cart = request.session.get('cart', {})
    if str(food_id) in cart:
        cart[str(food_id)] -= 1
        if cart[str(food_id)] <= 0:
            del cart[str(food_id)]
    request.session['cart'] = cart
    return redirect('view_cart')

def remove_from_cart(request, food_id):
    cart = request.session.get('cart', {})
    if str(food_id) in cart:
        del cart[str(food_id)]
    request.session['cart'] = cart
    return redirect('view_cart')

def view_cart(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0
    for food_id, quantity in cart.items():
        food = get_object_or_404(Food, pk=food_id)
        subtotal = food.price * quantity
        total += subtotal
        items.append({'food': food, 'quantity': quantity, 'subtotal': subtotal})
    return render(request, 'cart.html', {'items': items, 'total': total})