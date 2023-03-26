from datetime import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth import models as auth_models

from . import utils


# Create your models here.
class Entry(models.Model):
    user = models.ForeignKey(auth_models.User, on_delete=models.CASCADE)
    url = models.CharField(max_length=1024 * 4, null=False)
    unique_identifier = models.CharField(
        max_length=1024, null=False, default=utils.gen_tokipona_identifier
    )
    create_date = models.DateTimeField(default=timezone.now)
    last_update = models.DateTimeField(default=timezone.now)
    visits = models.IntegerField(default=0)
    enabled = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.url} --> {self.unique_identifier}"
