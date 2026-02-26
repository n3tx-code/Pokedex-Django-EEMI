from django.http import HttpResponse
from django.shortcuts import render

POKEMONS = (
    {"name": "Rondoudou", "type": 0},
    {"name": "Kyogre", "type": 1},
    {"name": "Lippoutou", "type": 3},
    {"name": "Tadmorv", "type": 2},
    {"name": "cliticlic", "type": 5},
)


def home(request):
    name = request.GET.get("name", "")
    if name:
        return HttpResponse(f"Hello {name}")

    return render(request, "home.html", {
        "sub_title": "Explorez le monde de Pokémon avec notre Pokedex complet. Trouvez des détails sur votre Pokémon préféré."})


def pika(request):
    return HttpResponse("Pika pika")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        return HttpResponse(f"Merci {name} pour ton message")
    return render(request, "contact.html")


def pokemon_detail(request, id):
    return render(request, "pokemon.html", {"pokemon": POKEMONS[id]})


def type_detail(request, id):
    types_pokemon = ["Normal", "Feu", "Eau", "Plante", "Électrik", "Glace", "Combat", "Poison", "Sol", "Vol", "Psy",
                     "Insecte", "Roche", "Spectre", "Dragon", "Ténèbres", "Acier", "Fée"]
    return render(request, "type.html", {"type": types_pokemon[id]})


def pokemon_list(request):
    return render(request, "pokemon_list.html", {"pokemons": POKEMONS})
