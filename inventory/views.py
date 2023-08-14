from django.shortcuts import render
from .forms import ProductUploadForm
from .models import Product
# from django.shortcuts import render

# Create your views here.
def product_upload(request):
    form = ProductUploadForm()
    return render(request,'inventory/product_upload.html',{'form': form})


def product_list(request):
    products=Product.objects.all()
    return render(request,"inventory/products_list.html",{"products":products})


def product_detail_view(request,id):
    product=Product.objects.get(id=id)
    return render(request,"inventory/product_details.html", {"product":product})

def edit_upload(request):
    form = ProductUploadForm()
    return render(request,'inventory/edit_upload.html',{'form': form})

            