from django.views import View
from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response
from rest_framework import generics
from core.models import *
from rest_framework.views import APIView
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


class ProfileListCreateAPIView(APIView):
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(
            instance=profiles,
            many=True
        )
        data = serializer.data
        return Response(data)

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            new_profile = serializer.save()
            new_serializer = ProfileSerializer(instance=new_profile)
            return Response(new_serializer.data, 201)

        return Response(serializer.errors, 400)


class ProfileDetailAPIView(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs["pk"]
        report = Profile.objects.get(id=id)
        serializer = ProfileSerializer(instance=report)
        return Response(serializer.data)


class ChildrenSectionListCreateAPIView(APIView):
    def get(self, request):
        sections = ChildrenSection.objects.all()
        serializer = ChildrenSectionSerializer(
            instance=sections,
            many=True
        )
        data = serializer.data
        return Response(data)

    def post(self, request):
        serializer = ChildrenSectionSerializer(data=request.data)
        if serializer.is_valid():
            new_section = serializer.save()
            new_serializer = ChildrenSectionSerializer(instance=new_section)
            return Response(new_serializer.data, 201)

        return Response(serializer.errors, 400)


class ChildrenSectionDetailAPIView(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs["pk"]
        section = ChildrenSection.objects.get(id=id)
        serializer = ChildrenSectionSerializer(instance=section)
        return Response(serializer.data)



