import google.generativeai as genai

from settings import API_KEY_PATH, MODEL_NAME
from myio import read_file

class Bot():

	def __init__(self):
		self._model = genai.GenerativeModel(
			model_name=MODEL_NAME,
			generation_config={
				"temperature": 0.3,
				"max_output_tokens": 2048,
			})
		self.load_apikey()

	def load_apikey(self):
		self._api_key = read_file(API_KEY_PATH).split('=')[1]
		genai.configure(api_key=self._api_key)
		return

	def send_prompt(self, prompt):
		try:
			response = self._model.generate_content(prompt).text
		except Exception as exc:
			response = None
			print(exc)
		return response




