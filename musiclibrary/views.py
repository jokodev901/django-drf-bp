from rest_framework import viewsets

from .models import Artist, Album, Track
from .serializers import ArtistSerializer, AlbumSerializer, TrackSerializer


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