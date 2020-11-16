from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('u1', views.unit1, name='unit1'),
]
