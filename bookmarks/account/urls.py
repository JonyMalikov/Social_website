from django.urls import path
from django.contrib.auth import views as auth_vievs

from . import views


urlpatterns = [
    # path("login/", views.user_login, name="login"),
    path("login/", auth_vievs.LoginView.as_view(), name="login"),
    path("logout/", auth_vievs.LogoutView.as_view(), name="logout"),
    path("", views.dashboard, name="dashboard"),
]
