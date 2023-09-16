from django.urls import path
from .views import *
urlpatterns = [
    path('', GetDataView.as_view(), name='home'),
    path('register/', CustomUserManagerView.as_view(), name='register'),
    path('profile-list/', ProfileListCreateView.as_view(), name='profile-list'),
    path('profile-detail/<int:pk>/', ProfileDetailCreateView.as_view(), name='profile-detail'),
    path('profiles/', ProfileListCreateAPIView.as_view(), name='profiles'),
    path('profiles/<int:pk>/', ProfileDetailAPIView.as_view(), name='profile'),
    path('sections/', ChildrenSectionListCreateAPIView.as_view(), name='sections'),
    path('sections/<int:pk>/', ChildrenSectionDetailAPIView.as_view(), name='section'),
]