from rest_framework import generics, status, views
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from User.models import NewUser
from User.serializers import NewUserSerializer, UserLoginSerializer


class RegisterView(generics.CreateAPIView):
    queryset = NewUser.objects.all()
    permission_classes = [AllowAny]
    serializer_class = NewUserSerializer

    def post(self, request):
        serializer = NewUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            new_user = NewUser.objects.get(email=request.data["email"])
            new_user.set_password(request.data["password"])
            new_user.save()
            if new_user:
                token = Token.objects.create(user=new_user)
                return Response(
                    {"token": token.key, "user": serializer.data},
                    status=status.HTTP_201_CREATED,
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(views.APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(NewUser, email=request.data["email"])
        if not user.check_password(request.data["password"]):
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {"token": token.key, "user": serializer.data}, status=status.HTTP_200_OK
        )


class TestTokenView(views.APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    def get(self, request):
        return Response({"detail": "Token is valid."}, status=status.HTTP_200_OK)
