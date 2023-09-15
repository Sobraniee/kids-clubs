from django.views import View
from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response
from rest_framework import generics
from core.models import *
from .serializers import *

class ProfileListCreateView(View):
    def get(self, request):
        context = {}
        context['profiles'] = Profile.objects.all()
        return render(request, context)


class ProfileDetailCreateView(View):
    def get(self, request, pk):
        try:
            profile = Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404("Profile does not exist")
        else:  # Add an else block
            context = {'profile': profile}
            return render(request, 'profile_detail.html', context)

