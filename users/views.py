from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer

User = get_user_model()


@api_view(["GET"])
def users_view(request):
    serializer = UserSerializer(User.objects.all(), many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
