from django.shortcuts import render
from .form import ReviewUploadForm
from .models import Review

# Create your views here.
def review_upload(request):
    form = ReviewUploadForm()
    return render(request,'review/review_upload.html',{'form': form})

def review_list(request):
    reviews=Review.objects.all()
    return render(request,"review/reviews_list.html",{"reviews":reviews})


def review_detail_view(request,id):
    review=Review.objects.get(id=id)
    return render(request,"review/review_details.html", {"review":review})
            