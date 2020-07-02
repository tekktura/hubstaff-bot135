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

    def __new__(cls):
        return cls.load()

    @classmethod
    def load(cls):
        with open(cls.SETTINGS_PATH, "r") as fp:
            return json.load(fp)

    def save(self):
        with open(self.SETTINGS_PATH, "w") as fp:
            return json.dump(self, fp)
