from django.shortcuts import render
from .forms import UpdateUserForm
from django.http import HttpResponseRedirect
from django.views.generic import UpdateView
from django.core.urlresolvers import reverse_lazy

def profile(UpdateView):
    if request.method == 'POST':
        form = UpdateUserForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/accounts/profile/')
    else:
        form = UpdateUserForm()
    
    return render(request, 'profile.html', {'form':form})

class UserUpdate(UpdateView):
        form_class = UpdateUserForm
        template_name = 'profile.html'
        success_url = reverse_lazy('profile')

        #get object
        def get_object(self, queryset=None): 
            return self.request.user



