from django.contrib import admin
from django.urls import include, path

from pokemon.views import contact, home

urlpatterns = [
    path("", home, name="homepage"),
    path("contact", contact, name="contact"), 
    path("pokemon/", include("pokemon.urls"))
]
