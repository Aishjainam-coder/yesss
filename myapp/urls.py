from django.urls import path
from myapp.views import *


urlpatterns = [
    path("members/", members, name="members"),
    path(" ", members, name="members"),
]
