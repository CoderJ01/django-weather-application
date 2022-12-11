from django.urls import path # allows for the specification of different urls
from . import views # import everything from the views.py file

# hold a list of all the urls the django site will have
urlpatterns = [
    path('', views.index, name="index")
]