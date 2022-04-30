from rest_framework import generics, permissions, serializers, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from business.models import Business
from business.serializers import (
    BusinessCreateSerializer,
    BusinessReviewsCreateSerializer,
    BusinessReviewsSerializer,
    BusinessSerializer,
)
from review.models import Review


class BusinessReviewsView(APIView):
    def get(self, *args, **kwargs):
        business = get_object_or_404(Business, pk=self.kwargs.get("business_id", ""))
        reviews = Review.objects.filter(business=business)
        serializer = BusinessReviewsSerializer(reviews, many=True)
        context = {
            "error": False,
            "message": f"{business.name} Reviews",
            "data": serializer.data,
        }
        return Response(context, status=status.HTTP_200_OK)


class BusinessReviewCreate(generics.CreateAPIView):
    serializer_class = BusinessReviewsCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        business = get_object_or_404(Business, pk=self.kwargs.get("business_id", ""))
        if business.owner == self.request.user:
            raise serializers.ValidationError("Permission Denied")
        serializer.save(business=business)


class BusinessList(APIView):
    def get(self, *args, **kwargs):
        businesses = Business.objects.all()
        serializer = BusinessSerializer(businesses, many=True)
        context = {"error": False, "message": "Businesses", "data": serializer.data}
        return Response(context, status=status.HTTP_200_OK)


class BusinessDetail(APIView):
    def get(self, *args, **kwargs):
        business = get_object_or_404(Business, pk=self.kwargs.get("business_id", ""))
        serializer = BusinessSerializer(business)
        context = {"error": False, "message": "Business", "data": serializer.data}
        return Response(context, status=status.HTTP_200_OK)


class BusinessReviewDetail(APIView):
    def get(self, *args, **kwargs):
        business = get_object_or_404(Business, pk=self.kwargs.get("business_id", ""))
        review = get_object_or_404(
            business.reviews.all(), pk=self.kwargs.get("review_id", "")
        )
        serializer = BusinessReviewsSerializer(review)
        context = {"error": False, "message": "Review", "data": serializer.data}
        return Response(context, status=status.HTTP_200_OK)


class BusinessCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = BusinessCreateSerializer

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


business_reviews_detail = BusinessReviewDetail.as_view()
business_reviews_create = BusinessReviewCreate.as_view()
business_reviews = BusinessReviewsView.as_view()
business_detail = BusinessDetail.as_view()
business_list = BusinessList.as_view()
business_create = BusinessCreate.as_view()
