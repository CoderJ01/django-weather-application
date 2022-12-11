from django.urls import path # allows for the specification of different urls
from . import views

urlpatterns = [
    path('', views.index, name="index")
]