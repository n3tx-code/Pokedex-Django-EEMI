from django.contrib import admin

from pokemon.models import Pokemon, PokemonType

# Register models with Django admin so they can be created/edited in the admin UI.
admin.site.register(Pokemon)
admin.site.register(PokemonType)
