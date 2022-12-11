from django.urls import path # allows for the specification of different urls
from . import views # import everything from the views.py file

urlpatterns = [
    path('', views.index, name="index")
]