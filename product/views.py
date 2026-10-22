
from django.shortcuts import render, get_object_or_404
from .models import Product


def shop(req):
    # products = Product.objects.filter(is_active=True)
    return render(req, "shop.html")


def details(req, slug):
    product = get_object_or_404(Product,slug=slug,is_active=True)
    return render(req,"product-details.html",{"product": product})
