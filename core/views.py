from django.http import JsonResponse
from rest_framework import generics

from .models import Profile, ProfileKid, Comment, Trainer, ChildrenSection
from .serializers import ProfileSerializer, ProfileKidSerializer, CommentSerializer, TrainerSerializer, ChildrenSectionSerializer

# Представление для создания и просмотра профилей
class ProfileListCreateView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# Представление для обновления, удаления и просмотра отдельного профиля
class ProfileRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# Представление для создания и просмотра профилей детей
class ProfileKidListCreateView(generics.ListCreateAPIView):
    queryset = ProfileKid.objects.all()
    serializer_class = ProfileKidSerializer

# Представление для обновления, удаления и просмотра отдельного профиля ребенка
class ProfileKidRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProfileKid.objects.all()
    serializer_class = ProfileKidSerializer

# Представление для создания, просмотра и удаления комментариев
class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

# Представление для обновления, удаления и просмотра отдельного комментария
class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

# Представление для создания, просмотра и удаления тренеров
class TrainerListCreateView(generics.ListCreateAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

# Представление для обновления, удаления и просмотра отдельного тренера
class TrainerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

# Представление для создания, просмотра и удаления секций для детей
class ChildrenSectionListCreateView(generics.ListCreateAPIView):
    queryset = ChildrenSection.objects.all()
    serializer_class = ChildrenSectionSerializer


def filtered_sections_view(request, club_kinds_value):
    try:
        filtered_sections = ChildrenSection.objects.filter(club_kinds=club_kinds_value)
        serializer = ChildrenSectionSerializer(filtered_sections, many=True)
        return JsonResponse({'filtered_sections': serializer.data})
    except ChildrenSection.DoesNotExist:
        return ({'error': 'Секции не найдены'})

# filtered_sections = ChildrenSection("sport")
# Представление для обновления, удаления и просмотра отдельной секции для детей
class ChildrenSectionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChildrenSection.objects.all()
    serializer_class = ChildrenSectionSerializer
