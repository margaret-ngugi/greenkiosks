from django.shortcuts import render
from .form import CartUploadForm
from .models import Cart


# Create your views here.
def cart_upload(request):
    form = CartUploadForm()
    return render(request,'cart/cart_upload.html',{'form': form})


def cart_list(request):
    carts=Cart.objects.all()
    return render(request,"cart/carts_list.html",{"carts":carts})


def cart_detail_view(request,id):
    cart=Cart.objects.get(id=id)
    return render(request,"cart/cart_details.html", {"cart":cart})

def edit_upload(request):
    form = CartUploadForm()
    return render(request,'cart/edit_upload.html',{'form': form})

            