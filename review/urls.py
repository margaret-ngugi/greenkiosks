from review.views import review_upload,review_list, review_detail_view
from django.urls import path

urlpatterns = [
  path("reviews/upload/", review_upload,name="review_upload_view"), 
  path("reviews/list", review_list,name="reviews_list"),
  path("reviews/<int:id>/", review_detail_view,name="review_details")   
]