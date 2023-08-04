from typing import Any, Dict, Optional
from django.db import models
from django.shortcuts import render

# Create your views here.

from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm , UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, Edit_Profile_Form, Password_changing_Form, ProfilePageForm
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import get_object_or_404
from Ourblog.models import Profile

 
class show_user_profile_ViewDetailView(DetailView):
    model = Profile
    template_name = "registration/show_user_profile.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        users = Profile.objects.all()
        context= super(show_user_profile_ViewDetailView, self).get_context_data(**kwargs)
        page_user = get_object_or_404(Profile, id = self.kwargs['pk'])
        context["page_user"] = page_user
        return context

class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = "registration/CreateProfilePage.html"
    

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
 



class PasswordsChangeView(PasswordChangeView):
    #  from_class = PasswordChangeForm
     from_class = Password_changing_Form
     template_name = "registration/change_pass.html"
     success_url = reverse_lazy("hom")

class UserRegisterView(generic.CreateView):
    # form_class = UserCreationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')
    form_class = SignUpForm

class UserEditView(generic.UpdateView):
    # form_class = UserChangeForm
    template_name = 'registration/Edit_Profile.html'
    success_url = reverse_lazy('hom')
    form_class = Edit_Profile_Form

    def get_object(self):
        return self.request.user