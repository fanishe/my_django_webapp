from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome into shop")

def unit1(request):
    return HttpResponse("<h1>This is my unit1 in the shop</h1>")

