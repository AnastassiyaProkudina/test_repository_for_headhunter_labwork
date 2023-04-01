from django.urls import path

from accounts.views import LoginView, logout_view

urlpatterns = [
    path("login/", LoginView.as_view(), name='login'),
    path("logout/", logout_view, name='logout'),
]
