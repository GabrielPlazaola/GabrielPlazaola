from django.shortcuts import get_list_or_404, render

import requests
import json

from django.http import HttpResponse
from django.template import loader


response1 = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/hello")
response2 = requests.get("http://api.citybik.es/v2/networks")
response3 = requests.get("https://baconipsum.com/api/?type=all-meat")
response4 = requests.get("https://random-data-api.com/api/cannabis/random_cannabis?size=20")
response5 = requests.get("https://api.isevenapi.xyz/api/iseven/6/")

def jprint(obj):
    text = json.dumps(obj, indent=4)
    return text

def primera(palabra):
    respuesta = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/" + str(palabra))
    apirespuesta = respuesta.json()
    return apirespuesta

def cuarta(cant):
    respuesta = requests.get("https://random-data-api.com/api/cannabis/random_cannabis?size=" + str(cant))
    apirespuesta = respuesta.json()
    return apirespuesta

def quinta(numb):
    respuesta = requests.get("https://api.isevenapi.xyz/api/iseven/"+ str(numb) +"/")
    apirespuesta = respuesta.json()
    return apirespuesta

api1 = response1.json()
api2 = response2.json()
api3 = response3.json()
api4 = response4.json()
api5 = response5.json()

responselist = [0, response1, response2, response3, response4, response5]
apilist = [0, api1, api2, api3, api4, api5, 0, 0]

def index(request):
    context = {'apilist': apilist}
    return render(request, 'apis.html', context)

def detail(request, api_id):
    if api_id == 1:
        try:
            valor = request.GET["word"]
            apiseleccionada = primera(valor)
        except:
            apiseleccionada = apilist[api_id]
    elif api_id == 4:
        try:
            valor = request.GET["cantidad"]
            apiseleccionada = cuarta(valor)
        except:
            apiseleccionada = apilist[api_id]
    elif api_id == 5:
        try:
            valor = request.GET['numero']
            apiseleccionada = quinta(valor)
        except:
            apiseleccionada = apilist[api_id]
    elif api_id == 6:
        apiseleccionada = apilist
    else:
        apiseleccionada = apilist[api_id]
    destino = str(api_id) + ".html"
    context = {'apiseleccionada': apiseleccionada}
    return render(request, destino, context)
