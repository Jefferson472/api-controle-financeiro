from http.client import ImproperConnectionState
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from contabilidade.views.Receita import ReceitaViewSet
from contabilidade.views.Despesa import DespesaViewSet


router = routers.DefaultRouter()
router.register('receita', ReceitaViewSet, basename='Receita')
router.register('despesa', DespesaViewSet, basename='Despesa')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
