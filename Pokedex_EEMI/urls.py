from django.contrib import admin
from django.urls import include, path

from pokemon.views import ContactView, HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="homepage"),
    path("contact", ContactView.as_view(), name="contact"),
    path("pokemon/", include("pokemon.urls")),
    path('admin/', admin.site.urls),
    path('user/', include("user.urls"))
]
