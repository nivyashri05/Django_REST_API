from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from simpleapp.views import UserViewSet, GetAuthToken

router = routers.DefaultRouter()
router.register('users', UserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', GetAuthToken.as_view()),
]






