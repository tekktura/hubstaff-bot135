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

    def __init__(self):
        super().__init__()
        with open(self.SETTINGS_PATH, "r") as fp:
            self.update(json.load(fp))

    def save(self):
        with open(self.SETTINGS_PATH, "w") as fp:
            return json.dump(self, fp, indent=4)
