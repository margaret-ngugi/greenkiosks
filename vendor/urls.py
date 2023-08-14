from vendor.views import vendor_upload,vendor_list, vendor_detail_view
from django.urls import path

urlpatterns = [
  path("vendors/upload/", vendor_upload,name="vendor_upload_view"), 
  path("vendors/list", vendor_list,name="vendors_list"),
  path("vendors/<int:id>/", vendor_detail_view,name="vendor_details")   
]