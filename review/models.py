from django.contrib.auth import get_user_model
from django.db import models

from business.models import Business

User = get_user_model()


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    business = models.ForeignKey(
        Business, on_delete=models.CASCADE, related_name="reviews"
    )
    rating = models.PositiveIntegerField(default=0)
    review = models.TextField()

    def __str__(self):
        return str(self.review)
