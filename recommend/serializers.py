from rest_framework.serializers import ModelSerializer
from .models import *

class RecommendSerializer(ModelSerializer):
    class Meta:
        model = Recommend
        fields = '__all__'

class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = ['answer']