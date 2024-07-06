from rest_framework import viewsets

from .serializers import UserSerializer, FriendSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Friend, User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FriendViewSet(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

class UserFriendsList(APIView):
    def get(self, request, user_id, format=None):
        # Fetching the user by id
        user = User.objects.get(id=user_id)
        friends = Friend.objects.filter(user=user)
        serializer = FriendSerializer(friends, many=True)
        return Response(serializer.data)
