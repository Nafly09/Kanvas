from django.urls import path

from users.views import AddressView, LoginView, UsersView


urlpatterns = [
    path("accounts/", UsersView.as_view()),
    path("login/", LoginView.as_view()),
    path("address/", AddressView.as_view())
]
