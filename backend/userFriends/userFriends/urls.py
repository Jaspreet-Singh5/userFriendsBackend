from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user.views import UserViewSet, FriendViewSet, UserFriendsList

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'friends', FriendViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/users/<int:user_id>/friends/', UserFriendsList.as_view(), name='user-friends'),
]
