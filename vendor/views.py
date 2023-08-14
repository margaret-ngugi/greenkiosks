from django.shortcuts import render
from .form import VendorUploadForm
from .models import Vendor

# Create your views here.
def vendor_upload(request):
    form = VendorUploadForm()
    return render(request,'vendor/vendor_upload.html',{'form': form})

def vendor_list(request):
    vendors=Vendor.objects.all()
    return render(request,"vendor/vendors_list.html",{"vendors":vendors})


def vendor_detail_view(request,id):
    vendor=Vendor.objects.get(id=id)
    return render(request,"vendor/vendor_details.html", {"vendor":vendor})