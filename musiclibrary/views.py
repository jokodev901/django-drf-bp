from rest_framework import viewsets, generics

from .models import Artist, Album, Track
from .serializers import ArtistSerializer, AlbumSerializer, TrackSerializer, ArtistTrackSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet example for the Artist model

    Implements a standard set of API methods to be routed into urlpattern

    list() - GET /artists
    retrieve() - GET /artists/<pk>
    create() - POST /artists/
    update() - PUT /artists/<pk>
    partial_update() - PATCH /artists/<pk>
    destroy() - DELETE /artists/<pk>
    """

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet example for the Album model

    Implements a standard set of API methods to be routed into urlpattern

    list() - GET /albums
    retrieve() - GET /albums/<pk>
    create() - POST /albums/
    update() - PUT /albums/<pk>
    partial_update() - PATCH /albums/<pk>
    destroy() - DELETE /albums/<pk>
    """

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    

class TrackViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet example for the Album model

    Implements a standard set of API methods to be routed into urlpattern

    list() - GET /tracks
    retrieve() - GET /tracks/<pk>
    create() - POST /tracks/
    update() - PUT /tracks/<pk>
    partial_update() - PATCH /tracks/<pk>
    destroy() - DELETE /tracks/<pk>
    """

    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class ArtistTrackList(generics.ListAPIView):
    """
    View intended for use with ArtistTrackSerializer to return all related tracks nested within each Artist

    Overridden get_queryset method adds in a prefetch condition for related tracks in order to avoid n+1 queries being
    executed.

    For comparison, use ArtistTrackListSlow to trigger n+1 case
    """
    serializer_class = ArtistTrackSerializer

    def get_queryset(self):
        queryset = Artist.objects.all()
        queryset = queryset.prefetch_related('tracks', 'tracks__artist')
        return queryset


class ArtistTrackListSlow(generics.ListAPIView):
    """
    View intended for use with ArtistTrackSerializer to return all related tracks nested within each Artist

    Uses stock ListAPIView with no modifications to demonstrate n+1 problem when querying related tracks
    """
    queryset = Artist.objects.all()
    serializer_class = ArtistTrackSerializer
