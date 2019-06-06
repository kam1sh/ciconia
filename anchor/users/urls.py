from anchor.users.views import (
    LoginPage,
    user_detail_view,
    user_list_view,
    user_redirect_view,
    user_update_view,
)
from django.urls import path

app_name = "users"
urlpatterns = [
    path("", view=user_list_view, name="list"),
    path("login/", view=LoginPage.as_view(), name="login"),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
