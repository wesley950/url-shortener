from django.urls import path

from . import views

urlpatterns = [path("<entry_uid>/", view=views.index, name="index")]
