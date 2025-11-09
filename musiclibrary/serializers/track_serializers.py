from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField
from ..models import Artist, Track


class TrackSerializer(serializers.ModelSerializer):
    artist = PrimaryKeyRelatedField(queryset=Artist.objects.all(), many=True, read_only=False)

    class Meta:
        model = Track
        fields = '__all__'
