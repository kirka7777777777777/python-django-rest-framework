# snippets/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

# Создаем router и регистрируем ViewSets
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename='snippet')
router.register(r'users', views.UserViewSet, basename='user')

# URL теперь определяются автоматически роутером
urlpatterns = [
    path('', include(router.urls)),
]