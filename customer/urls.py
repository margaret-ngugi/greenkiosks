from customer.views import customer_upload,customer_list, customer_detail_view
from django.urls import path

urlpatterns = [
  path("customers/upload/", customer_upload,name="customer_upload_view"),  
  path("customers/list", customer_list,name="customers_list"),
  path("customers/<int:id>/", customer_detail_view,name="customer_details") 
]


