from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('transportation', views.transportation, name='transportation'),
    path('diabetes', views.diabetes, name='diabetes'),
    path('nutrition', views.nutrition, name='nutrition'),
]

