from django.urls import path

from pokemon.views import pika, pokemon_detail, type_detail, pokemon_list

urlpatterns = [
    path("<int:id>", pokemon_detail, name="pokemon_detail"),
    path("liste", pokemon_list, name="pokemon_list"),
    path("pika", pika, name="pika"),
    path("type/<int:id>", type_detail, name="type_detail"),

]
