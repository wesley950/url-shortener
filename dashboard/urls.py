from django.urls import path

from . import views

urlpatterns = [
    path("", view=views.home, name="home"),
    path("dashboard/", view=views.dashboard, name="dashboard"),
    path("upsert_link/", view=views.upsert_link, name="upsert_link"),
    path("register/", view=views.register, name="register"),
    path("login/", view=views.login, name="login"),
    path("logout/", view=views.logout, name="logout"),
]
