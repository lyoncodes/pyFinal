from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
  path('', views.AccountView.as_view(), name="account"),
  path('login', views.SignInView.as_view(), name="login"),
  path('test', views.profile_view, name="test")
]