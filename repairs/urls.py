from django.urls import path
from . import views

urlpatterns = [
    path("", views.repair_list, name="repair_list"),
]