import requests

from bs4 import BeautifulSoup
from string import Template

def parse(html) -> tuple:
	"""
	Retorna o título e a descrição formatada da oferta de emprego de uma página Gupy.
	"""
	def refine(piece):
		"""
		Útil para obter texto de bloco HTML respeitando novos parágrafos e itens de lista.
		"""
		piece = piece.replace('<p><ul><li>', '\n- ').replace('<p>', '\n').replace('<li>', '\n- ')
		out = []
		for c in piece:
			if c == '<':
				to_write = False
			elif c == '>':
				to_write = True
			elif to_write:
				out.append(c)
		return ''.join(out)

	soup = BeautifulSoup(html, "html.parser")
	title = soup.find(id='h1').text
	out = [
		f"{outter_div.h2.text}\n{refine(str(outter_div.div))}\n"
		for outter_div in soup.section.children
		]
	return title, '\n'.join(out)

def get_page(url: str) -> str:
	"""
	Faz o download da página da vaga de emprego.
	"""
	response = requests.get(url)
	if response.status_code == 200:
		html_content = response.text.replace('\u00A0', ' ')
	else:
		raise RuntimeError(f"Error downloading webpage: {response.status_code}")
	return html_content
