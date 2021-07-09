from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import pf_ownership_required
from profileapp.forms import ProfileCreation
from profileapp.models import Profile

class PfCreate(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreation
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/create.html'

    def form_valid(self, form):
        temp_profile = form.save(commit=False)  #임시(데이터)로 저장
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)

@method_decorator(pf_ownership_required, 'get')
@method_decorator(pf_ownership_required, 'post')
class PfUpdate(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreation
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/update.html'