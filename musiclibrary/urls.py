from django.urls import path, include
from rest_framework.routers import DefaultRouter

from musiclibrary import views

router = DefaultRouter()

router.register(r'artists', views.ArtistViewSet, basename='artist')
router.register(r'albums', views.AlbumViewSet, basename='album')
router.register(r'tracks', views.TrackViewSet, basename='track')

urlpatterns = [
    path('', include(router.urls)),
    path('artisttracks/', views.ArtistTrackList.as_view()),
    path('slowartisttracks/', views.ArtistTrackListSlow.as_view()),
    path('spotifytest/', views.SpotifyTest.as_view()),
]