from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, FormView

from pokemon.forms import ContactForm
from pokemon.models import Pokemon, PokemonType


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sub_title"] = "Coucou ceci est le contenu de la varible de context sub_title"
        context["pokemon"] = Pokemon.objects.all().order_by("?").first()
        return context


def pika(request):
    return HttpResponse("Pika pika")


class ContactView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("homepage")

    def form_valid(self, form):
        '''
        Save all the message send from the contat form in the database :
        - create a model (make the migration and apply them)
        - save the model
        '''
        print('coucou')
        return super().form_valid(form)


class PokemonDetailView(DetailView):
    model = Pokemon
    template_name = "pokemon.html"


class TypeDetailView(DetailView):
    model = PokemonType
    template_name = "type.html"


class PokemonListView(ListView):
    model = Pokemon
    template_name = "pokemon_list.html"
