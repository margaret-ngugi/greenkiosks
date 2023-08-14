from delivery.views import delivery_upload,delivery_list, delivery_detail_view
from django.urls import path

urlpatterns = [
  path("deliverys/upload/", delivery_upload,name="delivery_upload_view"),  
  path("deliverys/list", delivery_list,name="deliverys_list"),
  path("deliverys/<int:id>/", delivery_detail_view,name="delivery_details") 
]
