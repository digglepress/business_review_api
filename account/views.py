from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from account.serializers import RegisterSerializer


class RegisterView(GenericAPIView):
    permission_classes = []
    serializer_class = RegisterSerializer

    def post(self, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(serializer.validated_data.get("password"))
            user.save()
            Token.objects.create(user=user)
            context = {
                "error": False,
                "message": "User Created",
                "data": serializer.data,
            }
            return Response(context, status=status.HTTP_201_CREATED)

        context = {
            "error": True,
            "message": "User Not Created",
            "data": serializer.errors,
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)


class LoginView(ObtainAuthToken):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        context = {"token": token.key, "user_id": user.pk}
        return Response(context, status=status.HTTP_200_OK)


register = RegisterView.as_view()
login = LoginView.as_view()
