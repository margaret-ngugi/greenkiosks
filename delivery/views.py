from django.shortcuts import render
from .form import DeliveryUploadForm
from .models import Delivery


# Create your views here.
def delivery_upload(request):
    form = DeliveryUploadForm()
    return render(request,'delivery/delivery_upload.html',{'form': form})

def delivery_list(request):
    deliverys=Delivery.objects.all()
    return render(request,"delivery/deliverys_list.html",{"deliverys":deliverys})


def delivery_detail_view(request,id):
    delivery=Delivery.objects.get(id=id)
    return render(request,"delivery/delivery_details.html", {"delivery":delivery})
            