from rest_framework import serializers
from ..models import Artist
from .track_serializers import TrackSerializer

class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = '__all__'


class ArtistTrackSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ['id', 'name', 'created_date', 'modified_date', 'tracks']
