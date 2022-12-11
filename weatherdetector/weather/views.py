from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q'+city+'&appid=3f2e409528a52056b62087fa623591ee').read() # send request to Open Weather API
        json_data = json.loads(res) # retrieve data after request is sent
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' +
            str(json_data['coord']['lat']),
            "temp": str(json_data['main'['temp']]) + 'k',
            "pressure": str(json_data['main']['presure']),
            "humidity": str(json_data['main']['presure']),
        }
    else:
        city = ''
    return render(request, 'index.html', {'city': city}) # request for index.html file in templates
