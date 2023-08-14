from cart.views import cart_upload,cart_list, cart_detail_view,edit_upload
from django.urls import path

urlpatterns = [
  path("carts/upload/", cart_upload,name="cart_upload_view"), 
  path("carts/list", cart_list,name="carts_list"),
  path("carts/<int:id>/", cart_detail_view,name="cart_details"), 
  path("carts/<int:id>/", edit_upload,name="cart_details") 
  
  
  
]
