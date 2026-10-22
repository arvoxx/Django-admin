from django.contrib import admin
from django.urls import path
from core.views import *
from product.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="home"),
    path('contact', contact, name="contact"),
    path('shop', shop, name="shop"),
    path('products/<slug:slug>/', details, name='product-item'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)