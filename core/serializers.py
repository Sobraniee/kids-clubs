from rest_framework import serializers
from core.models import *


class CustomUserManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserManager
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'username', 'first_name', 'last_name', 'email')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = ('trainer_name', 'trainer_last_name', 'trainer_description')


class ChildrenSectionSerializer(serializers.ModelSerializer):
    trainers = TrainerSerializer()

    class Meta:
        model = ChildrenSection
        fields = '__all__'

class ProfileKidSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileKid
        fields = '__all__'
