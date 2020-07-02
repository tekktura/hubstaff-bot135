import json
import requests

from .apps import API_BASE

class HubstaffApiClient():
    """
    Encalspulates all the communication with Hubstaff API.
    """
    def authenticate(self, app_token, username, password):
        """
        Calls the 'auth' endpoint and either returns a user object with auth token or an error
        """
        response = requests.post(
            API_BASE + "/auth",
            headers={"App-Token": app_token},
            data=dict(email=username, password=password)
        )
        response.raise_for_status()  # possible codes 401 and 403
        return response.json()
