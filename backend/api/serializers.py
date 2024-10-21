from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

# ORM - Object Relational Mapping
# We write normal python code
# and django converts it to SQL/json
# serializer converts python objects to json

# This class is used to interact with
#  User model from Django’s authentication system
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {
            "password": {"write_only": True} # no one can see the password
        }

    # Implement method to create user
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {
            "author": {"read_only": True},
        }