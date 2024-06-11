from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

# Create your views here.

def home(request):
    return HttpResponse("funcionando")


def user(request):
    url='http://172.31.100.20:8000/user'
    response = request.get(url)
    json_data = response.json()
    return JsonResponse(json_data)

def fastapi(request):
    url ='http://172.31.100.20:8000/'
    response = request.get(url)
    json_data = response.json()
    return JsonResponse(json_data)
    