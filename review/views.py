from django.contrib.auth import get_user_model
from rest_framework import generics, throttling

from review.models import Review
from review.serializers import ReviewSerializer

User = get_user_model()


class HomeView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    throttle_classes = [throttling.UserRateThrottle]

    def get_queryset(self):
        reviews = Review.objects.filter(user=self.request.user)
        return reviews


home_view = HomeView.as_view()
