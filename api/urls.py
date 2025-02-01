from django.urls import path
from . import views

urlpatterns = [
    path("api/profile/", views.get_info),
]
