from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecommendViewSet, generate_answer


router = DefaultRouter()
router.register(r'recommend', RecommendViewSet, basename='recommend')

urlpatterns = [
    path('', include(router.urls)),
    path("generate-answer/", generate_answer, name="generate_answer"),
]