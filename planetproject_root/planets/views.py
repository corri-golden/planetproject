import json
from django.http import JsonResponse
from django.shortcuts import render

# from planets.models import Planet
from planet_api.api import get_planet_by_id
from planet_api.api import get_films_by_id



def get_by_id(request, id):
    success, response = get_planet_by_id(id)
    # planet = Planet(
    #     planet_id=id,
    #     name=response['name'],
    #     diameter=int(response['diameter']),
    #     rotation_period=int(response['rotation_period']),            orbital_period=int(response['orbital_period']),
    #     gravity=response['gravity'],
    #     population=int(response['population']),
    #     climate=response['climate'],
    #     terrain=response['terrain'],
    #     surface_water=int(response['surface_water'])
    #     )          
    return JsonResponse(response, status=200)




    