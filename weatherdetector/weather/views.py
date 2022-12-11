from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html') # request for index.html file in templates
