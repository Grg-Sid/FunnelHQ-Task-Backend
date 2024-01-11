from rest_framework import generics, permissions

from core.models import Books, UserProfile
from core.serializers import UserProfileSerializer


class CreateUserProfile(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    http_method_names = ["post"]
