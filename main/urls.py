from django.contrib import admin
from django.urls import path
from main.views import index
from shop.views import shop

urlpatterns = [
    path('', index, name = 'index'),
    path('shop/', shop, name = 'shop'),
    path('admin/', admin.site.urls),
]
