from django.utils.translation import gettext_lazy as _

from rest_framework import generics, status, response

from .serializers import RegisterUserSerializer
from .utils import complete_signup

# Register, login, otp, resend_otp, refresh_token, forgot_password, change_password

class RegisterUserView(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        res = response.Response(
            {'detail': _('Verification e-mail sent.')},
            status=status.HTTP_201_CREATED,
            headers=headers,
        )
        return res

    def perform_create(self, serializer):
        user = serializer.save()
        complete_signup(user)
