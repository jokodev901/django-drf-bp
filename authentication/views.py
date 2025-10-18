from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
# from rest_framework_tracking.mixins import LoggingMixin

from knox.models import AuthToken
from knox.views import LogoutAllView, LogoutView

from django.utils import timezone

from .serializers import LoginUserSerializer, UserSerializer


class LoginAPI(generics.GenericAPIView):
    sensitive_fields = {'response'}
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        first_login = True

        if user.last_login:
            first_login = False

        response = Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1],
            "first_login": first_login
        })

        user.last_login = timezone.now()
        user.save(update_fields=['last_login'])

        return response


class LogoutAllAPI(LogoutAllView):
    pass


class LogoutAPI(LogoutView):
    pass
