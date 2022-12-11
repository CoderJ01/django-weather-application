from django.urls import path # allows for the specification of different urls
from . import views # import everything from the views.py file

# hold a list of all the urls the django site will have
urlpatterns = [
    path('', views.index, name="index") # homepage will be left blank, hence the blank single quotes
                                        # views.index means "go to the index function in views.py"
                                        # the name variable holds the name given to the url
]