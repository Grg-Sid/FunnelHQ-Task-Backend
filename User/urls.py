from django.urls import path, include

from User.views import RegisterView, UserLoginView, TestTokenView


urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("test-token/", TestTokenView.as_view(), name="test-token"),
]
