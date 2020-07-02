import json
import requests

from .apps import API_BASE

class HubstaffApiClient():
    """
    Encalspulates all the communication with Hubstaff API.
    """
    def __init__(self, app_token, auth_token=""):
        self.app_token = app_token
        self.auth_token = auth_token

    def _request(self, method, endpoint, data={}, params={}):
        response = requests.request(
            method,
            API_BASE + "/" + endpoint,
            headers={"App-Token": self.app_token, "Auth-Token": self.auth_token},
            data=data,
            params=params
        )
        response.raise_for_status()
        return response.json()

    def authenticate(self, username, password):
        """
        Call the 'auth' endpoint and return a user object with auth token.
        """
        return self._request("POST", "auth", data=dict(email=username, password=password))

    def list_projects(self):
        """
        Call the 'projects' endpoint to list all user projects.
        """
        return self._request("GET", "projects")

    def list_activities_for_date(self, date):
        """
        Call the 'activities' endpoint to list all activities between 'start' and 'stop' time.
        """
        return self._request("GET", "activities",
            params={"start_time": "2020-07-01 00:00:00", "stop_time": "2020-07-01 23:59:59"}
        )
