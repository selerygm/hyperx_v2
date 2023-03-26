from django.shortcuts import render
from shop.models import Product
from django.views.generic import ListView


def index(request):
    product = Product.objects.all()[:5]
    contex = {
        'pr': product,
    }
    return render(request, 'index.html', contex)
