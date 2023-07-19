from django.shortcuts import render
from .forms import ProductUploadForm
# from django.shortcuts import render

def upload_product(request):
    form = ProductUploadForm()
    return render(request, 'inventory/product_upload.html', {'form': form})

# Create your views here.
