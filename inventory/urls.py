from django.urls import path 
from .views import product_upload,product_list, product_detail_view

urlpatterns=[
    path("products/upload/", product_upload,name="product_upload"),
    path("products/list", product_list,name="products_list"),
    path("products/<int:id>/", product_detail_view,name="product_details")
]