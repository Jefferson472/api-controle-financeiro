from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from contabilidade import urls as contabilidade_urls

router = routers.DefaultRouter()

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("", include(contabilidade_urls)),
]
