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
    return render(request,"inventory/Products_list.html",{"products":products})


def product_detail_view(request,id):
    product=product.objects.get(id=id)
    return render(request,"inventory/product_details.html", {"product":product})
            