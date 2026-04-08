from django.urls import path

from user.views import SignUpView, UserLoginView, DashboardView

# Routes for authentication and the logged-in user area.
urlpatterns = [
    # Logged-in landing page.
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    # Account creation and login.
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
]
