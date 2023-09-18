from django.urls import path
from .views import (
    ProfileListCreateView,
    ProfileRetrieveUpdateDestroyView,
    ProfileKidListCreateView,
    ProfileKidRetrieveUpdateDestroyView,
    CommentListCreateView,
    CommentRetrieveUpdateDestroyView,
    TrainerListCreateView,
    TrainerRetrieveUpdateDestroyView,
    ChildrenSectionListCreateView,
    ChildrenSectionRetrieveUpdateDestroyView,
    filtered_sections_view,
)

urlpatterns = [
    # Маршруты для профилей
    path('profiles/', ProfileListCreateView.as_view(), name='profile-list'),
    path('profiles/<int:pk>/', ProfileRetrieveUpdateDestroyView.as_view(), name='profile-detail'),

    # Маршруты для профилей детей
    path('profile-kids/', ProfileKidListCreateView.as_view(), name='profile-kid-list'),
    path('profile-kids/<int:pk>/', ProfileKidRetrieveUpdateDestroyView.as_view(), name='profile-kid-detail'),

    # Маршруты для комментариев
    path('comments/', CommentListCreateView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentRetrieveUpdateDestroyView.as_view(), name='comment-detail'),

    # Маршруты для тренеров
    path('trainers/', TrainerListCreateView.as_view(), name='trainer-list'),
    path('trainers/<int:pk>/', TrainerRetrieveUpdateDestroyView.as_view(), name='trainer-detail'),

    # Маршруты для секций для детей
    path('children-sections/', ChildrenSectionListCreateView.as_view(), name='children-section-list'),
    path('children-sections/<int:pk>/', ChildrenSectionRetrieveUpdateDestroyView.as_view(), name='children-section-detail'),
    path('filtered_sections/<str:club_kinds_value>/', filtered_sections_view, name='filtered_sections'),
]