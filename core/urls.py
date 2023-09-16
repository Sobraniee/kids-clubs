from django.urls import path
from .views import *
urlpatterns = [
    path('register/', CustomUserManagerView.as_view(), name='register'),
]