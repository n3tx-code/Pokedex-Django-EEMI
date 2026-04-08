from django.db import models


# Represent a Pokemon entity in django ORM
class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    # A Pokemon can have multiple types (and a type can belong to many Pokemon).
    types = models.ManyToManyField("pokemon.PokemonType")

    def __str__(self):
        # Human-friendly representation used in admin and Django shell.
        return self.name


class PokemonType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        # Human-friendly representation used in admin and Django shell.
        return self.name
