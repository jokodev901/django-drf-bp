from rest_framework import serializers
from ..models import Album
from .track_serializers import TrackSerializer
from .artist_serializers import ArtistSerializer


class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)
    primary_artist = ArtistSerializer(required=False)

    class Meta:
        model = Album
        fields = '__all__'
