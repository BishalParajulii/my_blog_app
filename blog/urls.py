from . import views
from django.urls import path

urlpatterns = [
    path('' , views.index , name = "Home-page"),
    # path('like/<int:post_id>/', views.like_post, name='like_post'),
    
]