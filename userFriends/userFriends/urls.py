from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user.views import UserViewSet, FriendViewSet, UserFriendsList

# Initialize the default router for automatically determining the URL configuration for the API
router = DefaultRouter()

# Register the UserViewSet with the router
router.register(r'users', UserViewSet)

# Register the FriendViewSet with the router
router.register(r'friends', FriendViewSet)

# Define the URL patterns for the application
urlpatterns = [
    # URL pattern for the admin interface
    path('admin/', admin.site.urls),
    
    # URL pattern for the API, includes all routes registered with the router
    path('api/', include(router.urls)),
    
    # URL pattern for retrieving a user's friends list, expects a user_id parameter
    path('api/users/<int:user_id>/friends/', UserFriendsList.as_view(), name='user-friends'),
]
