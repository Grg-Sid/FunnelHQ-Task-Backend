import json
import time

from django.contrib.auth import get_user_model
from rest_framework import generics, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from core.models import Books, UserProfile
from core.serializers import UserProfileSerializer, BookSerializer
import core.utils as utils


class CreateUserProfile(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    http_method_names = ["post"]

    def post(self, request, *args, **kwargs):
        user_id = utils.get_user_id_from_token(request)
        request.data["user"] = user_id
        return self.create(request, *args, **kwargs)


class AddBookView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    http_method_names = ["post"]

    def post(self, request, *args, **kwargs):
        user_id = utils.get_user_id_from_token(request)
        request.data["user"] = user_id
        return self.create(request, *args, **kwargs)


class RecommendationView(views.APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    def post(self, request):
        user_id = utils.get_user_id_from_token(request)
        user = UserProfile.objects.get(user=user_id)
        bio = user.bio
        genre = user.genre
        fav_author = user.fav_author

        max_retries = 3
        retry_delay_seconds = 1

        for attempt in range(1, max_retries + 1):
            try:
                response = utils.get_recommendation(bio, genre, fav_author)
                response = json.loads(response)
                data = response.copy()

                for book in data["books"]:
                    book["user"] = user_id
                    serializer = BookSerializer(data=book)
                    if serializer.is_valid():
                        serializer.save()

                return Response(response, status=200)

            except Exception as e:
                print(f"Attempt {attempt} failed. Retrying...")
                time.sleep(retry_delay_seconds)

        return Response(
            {"error": "Max retries reached. Unable to process the request."}, status=500
        )


class GetBooks(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    http_method_names = ["get"]

    def get(self, request):
        user_id = utils.get_user_id_from_token(request)
        user = get_user_model(pk=user_id)
        books = user.books
