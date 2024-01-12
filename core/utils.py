from dotenv import load_dotenv
import os

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

import openai

load_dotenv()
API_KEY = os.environ.get("OPENAI_API_KEY")
print(API_KEY)
openai.api_key = API_KEY

PROMPT = "Only return the json object and nothing else I don't want any other text other than json Recommend me 4 books on the basis of these factors: bio  = {}, genre = {}, fav_author = {} and return it in a json format with the following keys: title, author, genre"


def get_recommendation(bio: str, genre: str, fav_author: str):
    prompt = PROMPT.format(bio, genre, fav_author)
    query = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}]
    )
    response = query.get("choices")[0]["message"]["content"]
    print(response.split("\n"))
    return response


def get_user_id_from_token(request):
    header = request.headers.get("Authorization").split(" ")
    if len(header) != 2:
        return Response(
            {"detail": "Token not found."}, status=status.HTTP_401_UNAUTHORIZED
        )
    token = header[1]
    try:
        user_id = Token.objects.get(key=token).user_id
        return user_id
    except Token.DoesNotExist:
        return Response(
            {"detail": "Token not found."}, status=status.HTTP_401_UNAUTHORIZED
        )
