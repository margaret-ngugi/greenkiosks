from django.shortcuts import render
from .form import CategoryUploadForm
from .models import Category


# Create your views here.
def category_upload(request):
    form = CategoryUploadForm()
    return render(request,'category/category_upload.html',{'form': form})

def category_list(request):
    categorys=Category.objects.all()
    return render(request,"category/categorys_list.html",{"categorys":categorys})


def category_detail_view(request,id):
    category=Category.objects.get(id=id)
    return render(request,"category/category_details.html", {"category":category})
            