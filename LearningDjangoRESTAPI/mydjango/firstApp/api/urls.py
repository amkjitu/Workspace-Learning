from django.urls import re_path as url
from .views import *

urlpatterns = [
    url('first',firstAPI),
    url('registration',registrationAPI),

]