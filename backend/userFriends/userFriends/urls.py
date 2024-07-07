from django.contrib import admin
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from user.views import UserViewSet, FriendViewSet, UserFriendsList

# Create a router and register our viewsets with it.
router = DefaultRouter()
# Register UserViewSet with the URL pattern 'users'
router.register(r'users', UserViewSet)
# Register FriendViewSet with the URL pattern 'friends'
router.register(r'friends', FriendViewSet)

# The API URLs are determined automatically by the router.
urlpatterns = [
    # URL pattern for the admin site
    url(r'^admin/', admin.site.urls),
    # Include the router-generated URLs under the 'api/' prefix
    url(r'^api/', include(router.urls)),
    # URL pattern for getting a user's friends list
    # This uses a regular expression to capture the user_id from the URL
    url(r'^api/users/(?P<user_id>\d+)/friends/$', UserFriendsList.as_view(), name='user-friends'),
]
