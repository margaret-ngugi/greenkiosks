from django.shortcuts import render, redirect
from .forms import ProductUploadForm
from .models import Product
from django.http import HttpResponse 

def product_upload(request):
    form = ProductUploadForm()
    return render(request, 'inventory/product_upload.html', {'form': form})

def product_list(request):
    products = Product.objects.all()
    return render(request, "inventory/products_list.html", {"products": products})

def product_detail_view(request, id):
    product = Product.objects.get(id=id)
    return render(request, "inventory/product_details.html", {"product": product})

def edit_upload(request):
    form = ProductUploadForm()
    return render(request, 'inventory/edit_upload.html', {'form': form})

def product_update_view(request, id):
    product = Product.objects.get(id=id)
    
    if request.method == 'POST':
        form = ProductUploadForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_detail_view", id=product.id)
    else:
        form = ProductUploadForm(instance=product)
    
    return render(request, "inventory/edit_details.html", {"form": form})

