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
        'name': product.name,
        'img': product.img,
        'description': product.description,
        'discsecond': product.discsecond,
        'discthirs': product.discthirs,
        'price': product.price,
    }
    return render(response, "cart.html", context)


class search(ListView):
    template_name = 'cart.html'
    context_object_name = 'cart'

    def get_queryset(self):
        return Product.objects.filter(name__iregex=self.request.GET.get('q'))
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context

