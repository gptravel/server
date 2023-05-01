from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *

class RecommendViewSet(ModelViewSet):
    queryset = Recommend
    serializer_class = RecommendSerializer