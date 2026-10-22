from django.shortcuts import render
from  product.models import Product

def index(req):
    data = Product.objects.all()
    return render(req, "index.html",{"products" : data})

def contact(req):
    return render(req, "contact.html")