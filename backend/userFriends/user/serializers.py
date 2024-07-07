from rest_framework import serializers
from .models import User, Friend

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model. Converts the User model instances into JSON format
    and validates data for creating or updating User instances.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'date_joined']
        # Specifies the model to be serialized and the fields to be included in the serialized data.

class FriendSerializer(serializers.ModelSerializer):
    """
    Serializer for the Friend model. Converts the Friend model instances into JSON format
    and validates data for creating or updating Friend instances.
    """
    class Meta:
        model = Friend
        fields = ['id', 'user', 'friend']
        # Specifies the model to be serialized and the fields to be included in the serialized data.
