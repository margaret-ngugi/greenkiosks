from django.shortcuts import render
from .forms import ProductUploadForm
# from django.shortcuts import render

# Create your views here.
def product_upload(request):
    form = ProductUploadForm()
    return render(request,'inventory/product_upload.html',{'form': form})