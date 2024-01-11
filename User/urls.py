from django.urls import path, include

from User.views import NewUserCreate, UserLoginView


urlpatterns = [
    path("register/", NewUserCreate.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
]
