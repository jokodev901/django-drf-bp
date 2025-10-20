from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from .models import Artist, Album, Track

class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = '__all__'


class TrackSerializer(serializers.ModelSerializer):
    artist = PrimaryKeyRelatedField(queryset=Artist.objects.all(), many=True, read_only=False)
    # artist = ArtistSerializer(many=True, read_only=True)
    # genre = serializers.StringRelatedField(read_only=True) # return the string representation vs pk

    class Meta:
        model = Track
        fields = '__all__'


class ArtistTrackSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ['id', 'name', 'created_date', 'modified_date', 'tracks']


class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)
    primary_artist = ArtistSerializer(required=False)

    class Meta:
        model = Album
        fields = '__all__'
