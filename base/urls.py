from django.urls import path
from .views import add, show

urlpatterns = [
    path("add", add),
    path("show", show),
]
