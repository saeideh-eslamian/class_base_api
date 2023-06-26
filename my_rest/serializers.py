from rest_framework.serializers import ModelSerializer
from .models import Articel

class ArticelSerializer(ModelSerializer):
    class Meta:
        model = Articel
        fields = "__all__"
