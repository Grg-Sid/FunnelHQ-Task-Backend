from rest_framework import generics, status, views
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from User.models import NewUser
from User.serializers import NewUserSerializer, UserLoginSerializer


class NewUserCreate(generics.CreateAPIView):
    queryset = NewUser.objects.all()
    serializer_class = NewUserSerializer
    permission_classes = [AllowAny]
    http_method_names = ["post"]


class UserLoginView(views.APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {"msg": "User logged in"}
        return Response(response, status=status.HTTP_200_OK)
