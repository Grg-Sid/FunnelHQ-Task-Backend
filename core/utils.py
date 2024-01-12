from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status


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
