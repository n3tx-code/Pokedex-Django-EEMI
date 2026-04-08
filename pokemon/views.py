from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView

from pokemon.forms import ContactForm
from pokemon.models import Pokemon, PokemonType


# Simple landing page built with a `TemplateView`.
# Adds a random Pokémon to the context for display on the homepage.
class HomeView(TemplateView):
    # Setting the template to use for the home page
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sub_title"] = "Coucou ceci est le contenu de la varible de context sub_title"
        context["pokemon"] = Pokemon.objects.all().order_by("?").first()
        return context


# Minimal function-based view
def pika(request):
    return HttpResponse("Pika pika")


# Contact page handled as a `FormView`
class ContactView(FormView):
    # Setting the template to use for the contact page      
    template_name = "contact.html"
    # Setting the form to use for the contact page
    form_class = ContactForm
    # Setting the success url to redirect to after the form is submitted
    success_url = reverse_lazy("homepage")

    def form_valid(self, form):
        '''
        Save all the message send from the contat form in the database :
        - create a model (make the migration and apply them)
        - save the model
        '''
        return super().form_valid(form)


# Detail pages for the two core models.
class PokemonDetailView(DetailView):
    # Setting the model to use for the pokemon detail page
    # Django will automatically generate the detail page for the model by making a query to the database by using the primary key from the url
    model = Pokemon
    # Setting the template to use for the pokemon detail page
    template_name = "pokemon/detail.html"


class TypeDetailView(DetailView):
    # Setting the model to use for the type detail page
    # Django will automatically generate the detail page for the model by making a query to the database by using the primary key from the url
    model = PokemonType
    # Setting the template to use for the type detail page
    template_name = "type.html"


class PokemonListView(ListView):
    # Setting the model to use for the pokemon list page
    # Django will automatically generate the list page for the model by making a query to the database and passing the objects to the template
    model = Pokemon
    # Setting the template to use for the pokemon list page
    template_name = "pokemon_list.html"


# CRUD views for Pokémon. `LoginRequiredMixin` protects create/update/delete.
class PokemonCreateView(LoginRequiredMixin, CreateView):
    # Setting the model to use for the pokemon create page
    model = Pokemon
    # Setting the template to use for the pokemon create page
    template_name = "pokemon/create.html"
    # Setting the fields to use for the pokemon creation form
    fields = ["name", "types"]

    def form_valid(self, form):
        # Application-level validation to prevent duplicate Pokémon names.
        if Pokemon.objects.filter(name=form.cleaned_data["name"]).exists():
            messages.add_message(self.request, messages.ERROR, "Un pokémon avec le même nom existe déjà")
            return super().form_invalid(form)
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect to the newly created Pokémon detail page and show a flash message.
        pokemon = Pokemon.objects.last()
        messages.add_message(self.request, messages.SUCCESS, "Pokemon crée")
        return reverse_lazy("pokemon_detail", kwargs={"pk": pokemon.id})


class PokemonUpdateView(LoginRequiredMixin, UpdateView):
    model = Pokemon
    fields = ["name", "types"]
    template_name = "pokemon/update.html"

    def get_success_url(self):
        # Redirect back to the updated Pokémon detail page and show a flash message.
        pokemon = self.object
        messages.add_message(self.request, messages.SUCCESS, "Pokemon mis à jour")
        return reverse_lazy("pokemon_detail", kwargs={"pk": pokemon.id})


class PokemonDeleteView(LoginRequiredMixin, DeleteView):
    model = Pokemon
    template_name = 'pokemon/delete.html'

    def get_success_url(self):
        # After deletion, go back to the list and show a confirmation message.
        pokemon = self.object
        messages.add_message(self.request, messages.SUCCESS, f"{pokemon.name} est mort")
        return reverse_lazy("pokemon_list")
