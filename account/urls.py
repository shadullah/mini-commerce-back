from rest_framework.routers import DefaultRouter

from django.urls import path,include
from .views import RegView,AllUserDetails, loginView

router = DefaultRouter()
router.register('all', AllUserDetails)


urlpatterns = [
    path("", include(router.urls)),
    path("register/", RegView.as_view(), name="register"),
    path("login/", loginView.as_view(), name="login")
]

