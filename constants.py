"""Constants of the app.

HELP: Text to exhibit when help is required.
PROMPT_FILE: Path to file with prompt model.
SETTINGS: Path to JSON file where settings will be read from.
"""
from myio import read_file


HELP = read_file("files\\help.txt")
PROMPT_FILE = "files\\prompt_model.md"
SETTINGS = 'settings.json'

