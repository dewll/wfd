from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ninja_extra import NinjaExtraAPI
from .api import api


urlpatterns = [
    path("api/", api.urls),
]