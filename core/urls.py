from django.urls import path, include

from core.views import CreateUserProfile

urlpatterns = [
    path("create-profile/", CreateUserProfile.as_view(), name="create-profile"),
]
