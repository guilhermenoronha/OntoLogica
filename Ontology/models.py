from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator
from CustomUser.models import CustomUser 

def index(request):
    return render(request, 'index.html')

class Ontology(models.Model):
    name = models.TextField(max_length=50)
    size = models.PositiveIntegerField(validators=[MaxValueValidator(5120)])
    date_added = models.DateTimeField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    file = models.FileField(default="")