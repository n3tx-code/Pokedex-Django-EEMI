from django.urls import path

from pokemon.views import pika, PokemonDetailView, PokemonListView, TypeDetailView

urlpatterns = [
    path("<int:pk>", PokemonDetailView.as_view(), name="pokemon_detail"),
    path("liste", PokemonListView.as_view(), name="pokemon_list"),
    path("pika", pika, name="pika"),
    path("type/<int:pk>", TypeDetailView.as_view(), name="type_detail"),
]
