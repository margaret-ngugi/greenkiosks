from django.urls import path 
from .views import product_upload,product_list, product_detail_view,product_update_view
from django.conf.urls.static import static

urlpatterns=[
    path("products/upload/", product_upload,name="product_upload"),
    path("products/list", product_list,name="products_list"),
    path("products/<int:id>/", product_detail_view,name="product_detail_view"),
    path("products/edit/<int:id>/", product_update_view,name="product_update"),
    
]
