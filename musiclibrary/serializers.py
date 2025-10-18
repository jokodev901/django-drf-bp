from rest_framework import serializers
from .models import Artist, Album, Track

class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = '__all__'


class TrackSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(many=True, read_only=True)
    genre = serializers.StringRelatedField(read_only=True) # return the string representation vs pk

    class Meta:
        model = Track
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)
    primary_artist = ArtistSerializer(required=False)

    class Meta:
        model = Album
        fields = '__all__'
