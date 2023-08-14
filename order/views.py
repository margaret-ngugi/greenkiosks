from django.shortcuts import render
from .form import OrderUploadForm
from .models import Order

# Create your views here.
def order_upload(request):
    form = OrderUploadForm()
    return render(request,'order/order_upload.html',{'form': form})

def order_list(request):
    orders=Order.objects.all()
    return render(request,"order/orders_list.html",{"orders":orders})


def order_detail_view(request,id):
    order=Order.objects.get(id=id)
    return render(request,"order/order_details.html", {"order":order})
            