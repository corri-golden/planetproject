from django.http import JsonResponse
from planet_api.api import *
import json
from django.shortcuts import render





# def home(request):
#     return HttpResponse("""
#     <h1>Welcome to Star Wars</h1>""")


def homepage(request):
    success, response = get_films()
    # planet = Planet(
    #     planet_id=id,
    #     name=response['name'],
    #     diameter=int(response['diameter']),
    #     rotation_period=int(response['rotation_period']),            
        # orbital_period=int(response['orbital_period']),
    #     gravity=response['gravity'],
    #     population=int(response['population']),
    #     climate=response['climate'],
    #     terrain=response['terrain'],
    #     surface_water=int(response['surface_water'])
    #     )          
    return JsonResponse(response, status=200)

def get_film(request, id):
    success, response = get_films_by_id(id)

    return JsonResponse(response, status=200)


   