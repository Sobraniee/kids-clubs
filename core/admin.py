from django.contrib import admin
from core.models import *


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email')

@admin.register(ProfileKid)
class ProfileKidAdmin(admin.ModelAdmin):
    list_display = ('id', 'kid_name', 'profile')

@admin.register(ChildrenSection)
class ChildrenSectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_club', 'description', 'club_kinds', 'record')

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('trainer_name', 'trainer_last_name')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'children_section')