from payment.views import payment_upload,payment_list, payment_detail_view
from django.urls import path

urlpatterns = [
  path("payments/upload/", payment_upload,name="payment_upload_view"),  
  path("payments/list", payment_list,name="payments_list"),
  path("payments/<int:id>/", payment_detail_view,name="payment_details")  
]