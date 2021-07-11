from django.shortcuts import render
from .models import Product, Location, ProductMovement
# Create your views here.


def base(request):
    return render(request,'inventory/base.html')


def prod(request):
    product = Product.objects.all()
    return render(request, 'inventory/product_detail.html',{'product': product})


def report(request):
    location = Location.objects.all()
    return render(request, 'inventory/Report.html', {'Location': location})


def product_movement(request):
    product_m = ProductMovement.objects.all()
    return render(request, 'inventory/Product_movement.html', {'product_m': product_m})