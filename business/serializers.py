from django.contrib.auth import get_user_model
from rest_framework import serializers

from business.models import Business
from review.models import Review
from users.serializers import UserSerializer

User = get_user_model()


class BusinessReviewsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ["rating", "review", "user"]


class BusinessReviewsCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Review
        fields = ["rating", "review", "user"]


class BusinessSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    reviews = BusinessReviewsSerializer(many=True, read_only=True)

    class Meta:
        model = Business
        fields = ["owner", "id", "name", "description", "reviews"]


class BusinessCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ["name", "description"]
