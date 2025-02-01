from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_info, name="home"),
    path("api/profile/", views.get_info, name="profile"),
]
