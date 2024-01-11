from django.contrib.auth import authenticate
from rest_framework import serializers

from User.models import NewUser


class NewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = (
            "id",
            "email",
            "user_name",
            "password",
            "first_name",
            "last_name",
        )
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        if NewUser.objects.filter(email=data["email"]).exists():
            raise serializers.ValidationError({"msg": "This email already exists"})
        if NewUser.objects.filter(user_name=data["user_name"]).exists():
            raise serializers.ValidationError({"msg": "This username already exists"})
        return data

    def create(self, validated_data):
        validated_data["is_active"] = True
        validated_data["is_staff"] = False
        NewUser.objects.create_user(**validated_data)
        return {"msg": "User created successfully"}


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)

        if not email or not password:
            raise serializers.ValidationError(
                {"msg": "Please provide email and password"}
            )

        user = authenticate(username=email, password=password)

        if not user:
            raise serializers.ValidationError({"msg": "Email does not exist"})

        if not user.check_password(password):
            raise serializers.ValidationError({"msg": "Wrong password"})

        if not user.is_active:
            raise serializers.ValidationError({"msg": "User is not active"})

        return user
