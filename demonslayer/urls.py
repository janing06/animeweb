from django.contrib import admin
from django.urls import path



from demonslayer.views import home,character,videos


urlpatterns = [

    path("",home, name="home"),
    path("character/",character, name="character"),
    path("videos/",videos, name="videos"),

] 