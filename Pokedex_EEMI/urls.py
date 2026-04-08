from django.contrib import admin
from django.urls import include, path

from pokemon.views import ContactView, HomeView

# Project-level URL routes:
urlpatterns = [
    # Public pages served directly by this project (class-based views).
    path("", HomeView.as_view(), name="homepage"),
    path("contact", ContactView.as_view(), name="contact"),

    # Delegate Pokémon feature URLs to the `pokemon` app.
    path("pokemon/", include("pokemon.urls")),

    # Django admin interface.
    path('admin/', admin.site.urls),

    # Delegate authentication/user-related URLs to the `user` app.
    path('user/', include("user.urls"))
]
