from django.shortcuts import render, redirect
def add_to_cart(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name', '').strip()
        try:
            item_cost = float(request.POST.get('item_cost', 0))
        except ValueError:
            return redirect('view_cart')
        if item_name and item_cost > 0:
            cart = request.session.get('cart', [])
            cart.append({'name': item_name, 'cost': item_cost})
            request.session['cart'] = cart
            request.session.modified = True
    return redirect('view_cart')

def view_cart(request):
    cart = request.session.get('cart', [])
    total_cost = sum(item['cost'] for item in cart)
    return render(request, 'shoppingcartapp/cart.html', {'cart': cart, 'total_cost': total_cost})
def clear_cart(request):
    request.session['cart'] = []
    request.session.modified = True
    return redirect('view_cart')
from django.db import models
class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.CharField(max_length=15)
