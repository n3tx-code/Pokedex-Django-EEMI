from django.urls import path

from pokemon.views import pika, PokemonDetailView, PokemonListView, TypeDetailView, PokemonCreateView, \
    PokemonUpdateView, PokemonDeleteView

urlpatterns = [
    path("<int:pk>", PokemonDetailView.as_view(), name="pokemon_detail"),
    path("liste", PokemonListView.as_view(), name="pokemon_list"),
    path("pika", pika, name="pika"),
    path("type/<int:pk>", TypeDetailView.as_view(), name="type_detail"),
    path('ajout', PokemonCreateView.as_view(), name='pokemon_add'),
    path('maj/<int:pk>', PokemonUpdateView.as_view(), name='pokemon_update'),
    path('suppression/<int:pk>', PokemonDeleteView.as_view(), name='pokemon_delete'),
]
