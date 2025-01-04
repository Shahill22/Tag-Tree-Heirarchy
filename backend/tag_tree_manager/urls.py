from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TreeNodeViewSet

router = DefaultRouter()
router.register('trees', TreeNodeViewSet, basename='trees')

urlpatterns = [
    path('', include(router.urls)),
]
