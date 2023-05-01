from rest_framework.serializers import ModelSerializer
from .models import Recommend

class RecommendSerializer(ModelSerializer):
    class Meta:
        model = Recommend
        fields = '__all__'
