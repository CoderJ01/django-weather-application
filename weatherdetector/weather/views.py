from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q'+city+'&appid=3f2e409528a52056b62087fa623591ee').read() # send request to Open Weather API
    else:
        city = ''
    return render(request, 'index.html', {'city': city}) # request for index.html file in templates
