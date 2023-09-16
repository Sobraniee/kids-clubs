from django.views import View
from django.shortcuts import render, redirect
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from django.http import JsonResponse
from .models import Comment
from rest_framework import status

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


class ProfileListCreateView(View):
    def get(self, request):
        context = {}
        context['profiles-list'] = Profile.objects.all()
        return render(request, context)

class ProfileDetailCreateView(View):
    def get(self, request, pk):
        try:
            profile = Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404("Profile does not exist")
        else:
            context = {'profile-detail': profile}
            return context

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

class ProfileKidListView(APIView):
    def get(self, request):
        profilekids = ProfileKid.objects.all()
        serializer = ProfileKidSerializer(
            instance=profilekids,
            many=True
        )
        data = serializer.data
        return Response(data)
    def post(self, request):
        serializer = ProfileKidSerializer(data=request.data)
        if serializer.is_valid():
            new_profilekid = serializer.save()
            new_serializer = ProfileKidSerializer(instance=new_profilekid)
            return Response(new_serializer.data, 201)

        return Response(serializer.errors, 400)

class CommentListAPIView(APIView):
    def get(self, request):
        comment = Comment.objects.all()
        serializer = CommentSerializer(
            instance=comment,
            many=True
        )
        data = serializer.data
        return Response(data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            new_comment = serializer.save()
            new_serializer = CommentSerializer(instance=new_comment)
            return Response(new_serializer.data, 201)

        return Response(serializer.errors, 400)

class TrainerListView(APIView):
    def get(self, request):
        trainer = Trainer.objects.all()
        serializer = TrainerSerializer(
            instance=trainer,
            many=True
        )
        data = serializer.data
        return Response(data)
    def post(self, request):
        serializer = TrainerSerializer(data=request.data)
        if serializer.is_valid():
            new_trainers = serializer.save()
            new_serializer = TrainerSerializer(instance=new_trainers)
            return Response(new_serializer.data, 201)

        return Response(serializer.errors, 400)

class ProfileKidDetailAPIView(APIView):
   def get(self, request, pk):
    try:
        profile_kid = ProfileKid.objects.get(pk=pk)
        data = {
            'kid_name': profile_kid.kid_name,
            'parent_profile': str(profile_kid.profile),
        }
        return JsonResponse(data)
    except ProfileKid.DoesNotExist:
        return JsonResponse({'error': 'Страница не найдено'}, status=404)

class CommmentDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            comment = Comment.objects.get(pk=pk)
            serializer = CommentSerializer(comment)
            return Response(serializer.data)
        except Comment.DoesNotExist:
            return Response({'error': 'Страница не найдено'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            comment = Comment.objects.get(pk=pk)
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Comment.DoesNotExist:
            return Response({'error': 'Страница не найдено'}, status=status.HTTP_404_NOT_FOUND)


class TrainerListCreateAPIView(APIView):
    def get(self, request):
        trainers = Trainer.objects.all()
        serializer = TrainerSerializer(
            instance=trainers,
            many=True
        )
        data = serializer.data
        return Response(data)

    def post(self, request):
        serializer = TrainerSerializer(data=request.data)
        if serializer.is_valid():
            new_trainer = serializer.save()
            new_serializer = TrainerSerializer(instance=new_trainer)
            return Response(new_serializer.data, 201)

        return Response(serializer.errors, 400)

class TrainerDetailAPIView(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs["pk"]
        trainer = Trainer.objects.get(id=id)
        serializer = TrainerSerializer(instance=trainer)
        return Response(serializer.data)