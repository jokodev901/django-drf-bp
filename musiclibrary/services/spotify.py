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


    def _refresh_token(self):
        if self.token:
            if datetime.now() < self.token_expiry:
                return

        response = requests.post(self.auth_url, data={'client_id': self.client_id,
                                                      'client_secret': self.client_secret,
                                                      'grant_type': 'client_credentials'})
        response.raise_for_status()
        self.token_expiry = datetime.now() + timedelta(seconds=response.json().get('expires_in'))
        self.token = response.json()['access_token']


    def artists(self):
        self._refresh_token()

        headers = {'Authorization': f'Bearer {self.token}'}
        response = requests.get(self.base_url + 'artists/4lgrzShsg2FLA89UM2fdO5', headers=headers)
        return response.json()
