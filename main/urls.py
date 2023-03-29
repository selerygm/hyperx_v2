from django.contrib import admin
from django.urls import path
from main.views import *
from shop.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # my pages
    path('', index, name='index'),
    path('shop/', shop, name='shop'),
    path('shop/headphones/', headphones, name='headphones'),
    path('shop/mouse/', mouse, name='mouse'),
    path('shop/monitors/', monitors, name='monitors'),
    path('shop/microphones/', microphones, name='microphones'),
    path('shop/keyboards/', keyboards, name='keyboards'),
    path('shop/<int:product_id>/', show_product, name='products'),
    path('search/', search.as_view(), name='search'),
    # admin
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)