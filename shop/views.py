from django.shortcuts import render
from shop.models import Product
from django.views.generic import ListView


def shop(request):
    product = Product.objects.all()
    contex = {
        'pr': product
    }
    return render(request, 'shop.html', contex)


def headphones(request):
    product = Product.objects.all()
    contex = {
        'pr': product
    }
    return render(request, 'headphones.html', contex)


def mouse(request):
    product = Product.objects.all()
    contex = {
        'pr': product
    }
    return render(request, 'mouse.html', contex)


def monitors(request):
    product = Product.objects.all()
    contex = {
        'pr': product
    }
    return render(request, 'monitors.html', contex)


def microphones(request):
    product = Product.objects.all()
    contex = {
        'pr': product
    }
    return render(request, 'microphones.html', contex)


def keyboards(request):
    product = Product.objects.all()
    contex = {
        'pr': product
    }
    return render(request, 'keyboards.html', contex)


def show_product(response, product_id):
    products = Product.objects.all()
    product = Product.objects.get(id=product_id)

    context = {
        'name': Product.name,
        'img': Product.img,
        'description': Product.description,
        'discsecond': Product.discsecond,
        'discthirs': Product.discthirs,
        'price': Product.price,
    }
    return render(response, "cart.html", context)
