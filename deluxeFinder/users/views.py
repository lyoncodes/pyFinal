from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.conf import settings
from django.http import JsonResponse
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView

from deluxeFinder.mixins import(
  AjaxFormMixin,
  FormErrors,
  RedirectParams,
)

from .forms import (
  UserForm,
  UserProfileForm,
  AuthForm,
)

# Create your views here.

class SignInView(FormView):
  '''
  Sign in form
  '''
  template_name = "registration/login.html"
  form_class = AuthForm
  success_url = "/"
  

def profile_view(request):
  '''
  profile view
  '''
  user = request.user
  prof = user.userprofile

  form = UserProfileForm(instance = prof)
  
  context = {'form': form}
  context['google_api_key'] = settings.GOOGLE_API_KEY
  context['base_country'] = "US"

  return render(request, 'users/profile.html', context)