from django.urls import path, include

from core.views import CreateUserProfile, AddBookView, RecommendationView

urlpatterns = [
    path("create-profile/", CreateUserProfile.as_view(), name="create-profile"),
    path("add-book/", AddBookView.as_view(), name="add-book"),
    path("recommend/", RecommendationView.as_view(), name="recommend"),
]
