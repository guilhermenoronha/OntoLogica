from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator
from CustomUser.models import CustomUser 
from django.core.exceptions import ValidationError 

def validate_file_extension(value):
    if value.file.content_type != 'application/xml' and not value.name.endswith('.owl'):
        raise ValidationError(u'File not supported.')

class Ontology(models.Model):
    name = models.TextField(max_length=50)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    file = models.FileField(default="", validators=[validate_file_extension])