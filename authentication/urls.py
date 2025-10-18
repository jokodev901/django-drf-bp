from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from .views import LoginAPI, LogoutAllAPI, LogoutAPI

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginAPI.as_view()),
    path('logout/', LogoutAPI.as_view()),
    path('logoutall/', LogoutAllAPI.as_view()),
]