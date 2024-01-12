from rest_framework import serializers
from core.models import Books, UserProfile
from django.contrib.auth import get_user_model


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            "id",
            "bio",
            "genre",
            "fav_author",
            "user",
        ]


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = [
            "id",
            "title",
            "author",
            "genre",
            "user",
        ]
