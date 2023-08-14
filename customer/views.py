from django.shortcuts import render
from .form import CustomerUploadForm
from .models import Customer

# Create your views here.
def customer_upload(request):
    form = CustomerUploadForm()
    return render(request,'customer/customer_upload.html',{'form': form})

def customer_list(request):
    customers=Customer.objects.all()
    return render(request,"customer/customers_list.html",{"customers":customers})


def customer_detail_view(request,id):
    customer=Customer.objects.get(id=id)
    return render(request,"customer/customer_details.html", {"customer":customer})

