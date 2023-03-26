from django.shortcuts import render, get_object_or_404
from django.http import (
    HttpResponseRedirect,
    HttpResponseNotAllowed,
    HttpResponseBadRequest,
)
from django.contrib import auth
from django.contrib.auth import models as auth_models
from django.contrib.auth import decorators
from django.utils import timezone

from redirecting import models as redirecting_models


def home(request):
    return render(request, "home.jinja", context={"title": "Home"})


@decorators.login_required(login_url="/login/")
def dashboard(request):
    return render(
        request,
        "dashboard.jinja",
        context={
            "title": "Dashboard",
            "links": redirecting_models.Entry.objects.filter(user=request.user),
        },
    )


@decorators.login_required(login_url="/login/")
def upsert_link(request):
    if request.method == "POST":
        url = request.POST.get("url")

        if not url:
            return HttpResponseBadRequest()

        entry = redirecting_models.Entry.objects.create(
            user=request.user,
            url=url,
        )
        entry.save()

    elif request.method == "GET":
        unique_identifier = request.GET.get("uniqueIdentifier")
        new_url = request.GET.get("newURL")
        toggle_state = request.GET.get("toggleState")
        delete = request.GET.get("delete")

        if not unique_identifier or (not new_url and not toggle_state and not delete):
            return HttpResponseBadRequest()

        url = get_object_or_404(
            redirecting_models.Entry,
            user=request.user,
            unique_identifier=unique_identifier,
        )

        if delete == "1":
            url.delete()
        else:
            if toggle_state == "1":
                url.enabled = not url.enabled
            if new_url:
                url.url = new_url
                url.last_update = timezone.now()
            url.save()

    else:
        return HttpResponseNotAllowed(["POST", "GET"])

    return HttpResponseRedirect("/dashboard/")


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password_confirmation = request.POST.get("passwordConfirmation")

        if password == password_confirmation:
            user = auth_models.User.objects.create_user(
                username=username, password=password
            )
            user.save()

            if user:
                auth.login(request, user)
                return HttpResponseRedirect("/dashboard/")

    return render(request, "register.jinja", context={"title": "Register"})


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(request, username=username, password=password)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect("/dashboard/")

    return render(request, "login.jinja", context={"title": "Login"})


@decorators.login_required(login_url="/login/")
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")
