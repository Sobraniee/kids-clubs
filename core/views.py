from django.shortcuts import render, redirect
from django.contrib import messages
from core.models import *
from django.views import View
from django.shortcuts import render, redirect
from .forms import RegistrationForm

class CustomUserManagerView(View):
    def register(request):
        if request.method == 'POST':
            form = CustomUserManager(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        else:
            CustomUserManager()
        return request