from django.urls import path
from . import views

urlpatterns = [
path('', views.posts_list), #posts_list is a callback function
]