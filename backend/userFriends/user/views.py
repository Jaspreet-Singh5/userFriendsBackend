from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, FriendSerializer
from .models import Friend, User

class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing User instances.
    """
    queryset = User.objects.all()  # Define the queryset to retrieve all User instances
    serializer_class = UserSerializer  # Specify the serializer to be used

class FriendViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Friend instances.
    """
    queryset = Friend.objects.all()  # Define the queryset to retrieve all Friend instances
    serializer_class = FriendSerializer  # Specify the serializer to be used

class UserFriendsList(APIView):
    """
    API view to retrieve a list of friends for a specific user.
    """
    def get(self, request, user_id, format=None):
        """
        Get method to fetch the list of friends for a given user.

        Args:
            request: The HTTP request object.
            user_id: The ID of the user whose friends are to be retrieved.
            format: The format in which the response is to be returned (optional).

        Returns:
            Response: A Response object containing the serialized data of the friends.
        """
        # Fetching the user by id
        user = User.objects.get(id=user_id)
        
        # Fetching friends of the user
        friends = Friend.objects.filter(user=user)
        
        # Serializing the friends data
        serializer = FriendSerializer(friends, many=True)
        
        # Returning the serialized data as a response
        return Response(serializer.data)
