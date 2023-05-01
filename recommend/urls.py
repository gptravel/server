from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecommendViewSet

router = DefaultRouter()
router.register(r'recommend/', RecommendViewSet, basename='recommend')

urlpatterns = [
    path('', include(router.urls)),
]