import json

from constants import SETTINGS


class Settings:
    """Settings defined in JSON file, accessed as an object."""

    def __init__(self):
        """Load settings from JSON source file."""
        try:
            with open(SETTINGS, encoding='utf8') as file:
                data = json.load(file)
        except:
            raise Exception(
                f"Settings could not be loaded from file: {SETTINGS}.")

        for key, value in data.items():
            setattr(self, key, value)

        return

