import requests

from datetime import datetime, timedelta
from django.conf import settings


class Spotify:
    def __init__(self):
        self.base_url = settings.SPOTIFY_BASE_URL
        self.auth_url = settings.SPOTIFY_AUTH_URL
        self.client_id = settings.SPOTIFY_CLIENT_ID
        self.client_secret = settings.SPOTIFY_CLIENT_SECRET
        self.token_expiry = None
        self.token = None


    def _build_headers(self):
        if not self.token or (datetime.now() < self.token_expiry):
            response = requests.post(self.auth_url, data={'client_id': self.client_id,
                                                          'client_secret': self.client_secret,
                                                          'grant_type': 'client_credentials'})
            response.raise_for_status()
            self.token_expiry = datetime.now() + timedelta(seconds=response.json().get('expires_in'))
            self.token = response.json()['access_token']

        return {'Authorization': f'Bearer {self.token}'}


    def artists(self, artist_id):
        headers = self._build_headers()

        response = requests.get(self.base_url + f'artists/{artist_id}', headers=headers)
        return response.json()


    def search(self, q, search_type, include_external, market, limit, offset):
        """
        You can narrow down your search using field filters.
         The available filters are album, artist, track, year, upc, tag:hipster, tag:new, isrc, and genre.
          Each field filter only applies to certain result types.

        The artist and year filters can be used while searching albums, artists and tracks.
            You can filter on a single year or a range (e.g. 1955-1960).
        The album filter can be used while searching albums and tracks.
        The genre filter can be used while searching artists and tracks.
        The isrc and track filters can be used while searching tracks.
        The upc, tag:new and tag:hipster filters can only be used while searching albums.
            The tag:new filter will return albums released in the past two weeks
             and tag:hipster can be used to return only albums with the lowest 10% popularity.

        Example: q=remaster%2520track%3ADoxy%2520artist%3AMiles%2520Davis


        multiple filters work, example 2 artists will return tracks with both artists listed
        so maybe expect dictionary of list items, artist: [] etc
        then build out q object by unpacking
        """


        headers = self._build_headers()

        pass