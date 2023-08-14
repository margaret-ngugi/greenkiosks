from order.views import order_upload,order_list, order_detail_view
from django.urls import path

urlpatterns = [
  path("orders/upload/", order_upload,name="order_upload_view"), 
  path("orders/list", order_list,name="orders_list"),
  path("orders/<int:id>/", order_detail_view,name="order_details")  
]