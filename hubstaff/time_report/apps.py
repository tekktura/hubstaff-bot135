import os.path
import json
from django.apps import AppConfig


API_BASE = "https://api.hubstaff.com/v1/"
SETTINGS_FILE = "settings.json"

class TimeReportConfig(AppConfig):
    name = 'time_report'

class Settings(dict):
    """
    Encapsulate settings file as dict operations
    """
    SETTINGS_PATH = os.path.join(os.path.dirname(__file__), SETTINGS_FILE)

    def load(self):
        with open(self.SETTINGS_PATH, "r") as fp:
            self = json.load(fp)
            return self

    def save(self):
        with open(self.SETTINGS_PATH, "w") as fp:
            return json.dump(self, fp, indent=4)
