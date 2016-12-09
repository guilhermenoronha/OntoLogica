from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadOntologyForm
from django.views.generic import CreateView

def index(request):
    if request.method == 'POST':
        form = UploadOntologyForm(request.POST, request.FILES)
        if form.is_valid():
            ontology = form.save(commit=False)
            ontology.name = request.FILES['file'].name
            ontology.user = request.user
            ontology.save()
            return HttpResponseRedirect('/ontology/')
    else:
          form = UploadOntologyForm()
    
    return render(request, 'index.html', {'form': form})
        