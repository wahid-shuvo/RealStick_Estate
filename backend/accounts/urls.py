from django.urls import path
from .views import SignupView
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('signup', csrf_exempt(SignupView.as_view())),
]