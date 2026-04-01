from django.db import models


class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    types = models.ManyToManyField("pokemon.PokemonType")

    def __str__(self):
        return self.name


class PokemonType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
