"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile-list/', ProfileListCreateView, name='profile-list/'),
    path('profile-detail/<int:pk>/', ProfileDetailCreateView, name='profile-detail/'),
    path('profiles/', ProfileListCreateAPIView.as_view(),name='profiles'),
    path('profiles/<int:pk>/', ProfileDetailAPIView.as_view(),name='profile'),
    path('sections/', ChildrenSectionListCreateAPIView.as_view(),name='sections'),
    path('sections/<int:pk>/', ChildrenSectionDetailAPIView.as_view(),name='section'),
]
