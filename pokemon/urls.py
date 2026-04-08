from django.urls import path

from pokemon.views import pika, PokemonDetailView, PokemonListView, TypeDetailView, PokemonCreateView, \
    PokemonUpdateView, PokemonDeleteView

# App-level URL routes for the pokemon app with a prefix of "pokemon/" (cf. Pokedex_EEMI/urls.py)
urlpatterns = [
    path("<int:pk>", PokemonDetailView.as_view(), name="pokemon_detail"),
    path("liste", PokemonListView.as_view(), name="pokemon_list"),
    # Simple demo endpoint.
    path("pika", pika, name="pika"),
    path("type/<int:pk>", TypeDetailView.as_view(), name="type_detail"),
    path('ajout', PokemonCreateView.as_view(), name='pokemon_add'),
    path('maj/<int:pk>', PokemonUpdateView.as_view(), name='pokemon_update'),
    path('suppression/<int:pk>', PokemonDeleteView.as_view(), name='pokemon_delete'),
]
