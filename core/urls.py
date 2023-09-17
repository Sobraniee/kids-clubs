from django.urls import path
from .views import *
urlpatterns = [
    path('register/', CustomUserManagerView.as_view(), name='register'),
    path('profile-list/', ProfileListCreateView.as_view(), name='profile-list'),
    path('profile-detail/<int:pk>/', ProfileDetailCreateView.as_view(), name='profile-detail'),
    path('profiles/', ProfileListCreateAPIView.as_view(), name='profiles'),
    path('profiles/<int:pk>/', ProfileDetailAPIView.as_view(), name='profile'),
    path('sections/', ChildrenSectionListCreateAPIView.as_view(), name='sections'),
    path('sections/<int:pk>/', ChildrenSectionDetailAPIView.as_view(), name='section'),
    path('profile-kids/', ProfileKidListView.as_view(), name='profile-kids'),
    path('profile-kids/<int:pk/', ProfileKidDetailAPIView.as_view(), name='profile-kid-detail-api'),
    path('comments/', CommentListAPIView.as_view(), name='comments'),
    path('api/comments/<int:pk>/', CommmentDetailAPIView.as_view(), name='comment-detail-api'),
    path('trainers/', TrainerListCreateAPIView.as_view(), name='trainers'),
    path('trainers/<int:pk>/', TrainerDetailAPIView.as_view(), name='trainer'),
]