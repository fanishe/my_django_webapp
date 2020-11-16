from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome into articles")

def art1(request):
    return HttpResponse("<h1>Welcome into art 1</h1>")

