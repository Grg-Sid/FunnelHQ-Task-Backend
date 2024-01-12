import os
from rest_framework import generics, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
import openai

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


PROMPT = "Only return the json object and nothing else Recommend me 4 books on the basis of these factors: bio  = {}, genre = {}, fav_author = {} and return it in a json format with the following keys: title, author, genre"


class RecommendationView(views.APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    def post(self, request):
        user_id = utils.get_user_id_from_token(request)
        user = UserProfile.objects.get(user=user_id)
        bio = user.bio
        genre = user.genre
        fav_author = user.fav_author
        prompt = PROMPT.format(bio, genre, fav_author)
        openai.api_key = os.environ.get("API_KEY")
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            temperature=0.3,
            max_tokens=60,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=["\n"],
        )
        data = response.choices[0].text.split("\n")
        data["user"] = user_id
        serializer = BookSerializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"detail": response.choices[0].text}, status=200)
