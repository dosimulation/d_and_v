from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('transportation', views.transportation, name='transportation'),
    path('diabetes', views.diabetes, name='diabetes'),
    path('nutrition', views.nutrition, name='nutrition'),
    path('login/', views.login_view, name='login'),
    path('login/submit/', views.login_submit_view, name='login_submit'),
    path('logout/', views.logout_view, name='logout'),
]

