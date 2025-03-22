from django.shortcuts import render
from .models import Product
from django.http import HttpResponse

def product_list(request):
    products = [
        {
            'name':'laptop','description':'High-end quality','price':60000
        }
    ]
    return render(request, 'bootstrap_app/products.html', {'products': products})