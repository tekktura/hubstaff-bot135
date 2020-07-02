import datetime
import requests

from .apps import API_BASE


class HubstaffApiClient():
    """
    Encaspulates all the communication with Hubstaff API.
    """
    def __init__(self, app_token, auth_token=""):
        self.app_token = app_token
        self.auth_token = auth_token

    def _request(self, method, endpoint, data={}, params={}):
        response = requests.request(
            method,
            API_BASE + "/" + endpoint,
            headers={"App-Token": self.app_token,
                     "Auth-Token": self.auth_token,
                     "Accept": "application/json"},
            data=data,
            params=params
        )
        response.raise_for_status()
        return response.json()

    def authenticate(self, username, password):
        """
        Call the 'auth' endpoint and return a user object with auth token.
        """
        return self._request("POST", "auth",
                             data={"email": username, "password": password}).get("user", {})

    def list_projects(self):
        """
        Call the 'projects' endpoint to list all user projects.
        """
        return self._request("GET", "projects").get("projects", {})

    def list_users(self):
        """
        Call the 'users' endpoint to list all user.
        """
        return self._request("GET", "users").get("users", {})

    def list_activities_for_date(self, date):
        """
        Call the 'activities' endpoint to list all activities between 'start' and 'stop' time.
        """
        # calculate timespan for one day equal to 'date
        start = datetime.datetime.combine(date, datetime.time(0, 0, 0))
        end = datetime.datetime.combine(date, datetime.time(23, 59, 59))
        return self._request("GET", "activities",
                             params={"start_time": start.isoformat(), "stop_time": end.isoformat()}
                            ).get("activities", {})