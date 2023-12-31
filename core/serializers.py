from rest_framework import serializers
from .models import Profile, ProfileKid, Comment, Trainer, ChildrenSection

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = '__all__'

class ChildrenSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildrenSection
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class ProfileKidSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileKid
        fields = '__all__'
