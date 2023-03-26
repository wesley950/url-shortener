from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound

from . import models


def index(request, entry_uid: str):
    entry = get_object_or_404(models.Entry, unique_identifier=entry_uid)

    if entry.enabled and entry.user.is_active:
        entry.visits += 1
        entry.save()
        return HttpResponseRedirect(redirect_to=entry.url)

    return HttpResponseNotFound()
