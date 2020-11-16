from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('a1', views.art1, name='art1'),
]
