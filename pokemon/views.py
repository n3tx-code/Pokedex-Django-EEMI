from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView

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
    template_name = "pokemon/detail.html"


class TypeDetailView(DetailView):
    model = PokemonType
    template_name = "type.html"


class PokemonListView(ListView):
    model = Pokemon
    template_name = "pokemon_list.html"


class PokemonCreateView(LoginRequiredMixin, CreateView):
    model = Pokemon
    template_name = "pokemon/create.html"
    fields = ["name", "types"]

    def form_valid(self, form):
        if Pokemon.objects.filter(name=form.cleaned_data["name"]).exists():
            messages.add_message(self.request, messages.ERROR, "Un pokémon avec le même nom existe déjà")
            return super().form_invalid(form)
        return super().form_valid(form)

    def get_success_url(self):
        pokemon = Pokemon.objects.last()
        messages.add_message(self.request, messages.SUCCESS, "Pokemon crée")
        return reverse_lazy("pokemon_detail", kwargs={"pk": pokemon.id})


class PokemonUpdateView(LoginRequiredMixin, UpdateView):
    model = Pokemon
    fields = ["name", "types"]
    template_name = "pokemon/update.html"

    def get_success_url(self):
        pokemon = self.object
        messages.add_message(self.request, messages.SUCCESS, "Pokemon mis à jour")
        return reverse_lazy("pokemon_detail", kwargs={"pk": pokemon.id})


class PokemonDeleteView(LoginRequiredMixin, DeleteView):
    model = Pokemon
    template_name = 'pokemon/delete.html'

    def get_success_url(self):
        pokemon = self.object
        messages.add_message(self.request, messages.SUCCESS, f"{pokemon.name} est mort")
        return reverse_lazy("pokemon_list")
