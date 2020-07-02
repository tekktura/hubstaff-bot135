import json
import requests

from .apps import API_BASE

class HubstaffApiClient():
    """
    Encalspulates all the communication with Hubstaff API.
    """
    def __init__(self, app_token, auth_token=None):
        self.app_token = app_token
        self.auth_token = auth_token

    def authenticate(self, username, password):
        """
        Call the 'auth' endpoint and either returns a user object with auth token or an error
        """
        response = requests.post(
            API_BASE + "/auth",
            headers={"App-Token": self.app_token},
            data=dict(email=username, password=password)
        )
        response.raise_for_status()  # possible codes 401 and 403
        return response.json()

    def list_user_projects(self, id):
        """
        Call the 'projects' endpoint to list al user projects.
        """
        response = requests.get(
            API_BASE + "/users/{}/projects".format(id),
            headers={"App-Token": self.app_token, "Auth-Token": self.app_token},
        )
        response.raise_for_status()  # possible codes 401, 403, 404
        return response.json()