from django.urls import path
from .views import *

urlpatterns = [
    path("", home),
    path("and/", andijon),
    path("far/",fargona),
    path("foot/", foot)
]