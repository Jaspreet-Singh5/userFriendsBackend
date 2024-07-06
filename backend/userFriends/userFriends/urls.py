from django.contrib import admin
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from user.views import UserViewSet, FriendViewSet, UserFriendsList

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'friends', FriendViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api/users/(?P<user_id>\d+)/friends/$', UserFriendsList.as_view(), name='user-friends'),
]
