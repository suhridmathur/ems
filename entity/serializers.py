from entity.models import Entity

from rest_framework.serializers import ModelSerializer

class EntitySerializer(ModelSerializer):
    """
    ModelSerializer class for Entity
    """
    class Meta:
        model = Entity
        fields = '__all__'