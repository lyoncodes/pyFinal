from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
  path('profile', views.profile_view, name="profile"),
  # path('login', views.SignInView.as_view(), name="login"),
]