from rest_framework import serializers
from .models import Generation


class GenerationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    timestamp = serializers.DateTimeField()
    megawatts = serializers.FloatField()
    market = serializers.CharField()
    fuel = serializers.SlugRelatedField(read_only=True, slug_field='name')
