from django.shortcuts import render
from .form import PaymentUploadForm
from .models import Payment

# Create your views here.
def payment_upload(request):
    form = PaymentUploadForm()
    return render(request,'payment/payment_upload.html',{'form': form})

def payment_list(request):
    payments=Payment.objects.all()
    return render(request,"payment/payments_list.html",{"payments":payments})


def payment_detail_view(request,id):
    payment=Payment.objects.get(id=id)
    return render(request,"payment/payment_details.html", {"payment":payment})
            