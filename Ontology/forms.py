from django import forms
from .models import Ontology
from django.core.exceptions import ValidationError  

class UploadOntologyForm(forms.ModelForm):
    class Meta:
        model = Ontology
        fields = ('file',)
    
    def clean_file(self):
        file = self.cleaned_data['file']

        try:
            if len(file) > (5000 * 1024):
                raise forms.ValidationError(u'File size can\'t exceed 5mb!')
        except AttributeError:
            pass
        
        return file

