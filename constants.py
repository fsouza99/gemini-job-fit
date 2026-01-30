"""Constants of the app.

HELP: Text to exhibit when help is required.
PROMPTS: Paths to distinct prompt model files.
SETTINGS: Path to JSON file where settings will be read from.
"""
from myio import read_file


HELP = read_file('files\\help.txt')
PROMPTS = {
	'a': 'files\\prompts\\advice.md',
	'f': 'files\\prompts\\fitness.md',
}
SETTINGS = 'settings.json'
