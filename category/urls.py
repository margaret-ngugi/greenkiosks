from category.views import category_upload,category_list, category_detail_view
from django.urls import path

urlpatterns = [
  path("categorys/upload/", category_upload,name="category_upload_view"),  
  path("categorys/list", category_list,name="categorys_list"),
  path("categorys/<int:id>/", category_detail_view,name="category_details") 
]


