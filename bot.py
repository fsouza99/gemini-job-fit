import google.generativeai as genai

from settings import API_KEY_PATH
from myio import read_file

class Bot():

	def __init__(self):
		self._model = genai.GenerativeModel('gemini-pro')
		self.last_prompt = self.last_response = None
		self.set_auto_apikey()

	def set_auto_apikey(self):
		self._api_key = read_file(API_KEY_PATH).split('=')[1]
		genai.configure(api_key=self._api_key)
		return

	def send_prompt(self, prompt):
		try:
			response = self._model.generate_content(prompt).text
		except Exception as exc:
			response = None
			print(exc)
		self.last_prompt = prompt
		self.last_response = response
		return response




