from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    institution = models.TextField(max_length=254)