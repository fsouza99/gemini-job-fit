import re
import requests

from bs4 import BeautifulSoup

def parse(html: str) -> tuple[str, str]:
	"""
	Retorna título e descrição formatada da oferta de emprego de uma página Gupy.
	"""
	def refine(piece):
		"""
		Obtém texto de bloco HTML respeitando novos parágrafos e itens de lista.
		"""
		piece = piece.replace('<p', '\n<p').replace('<li', '\n- <li')
		return re.sub(r"<(.*?)>", '', piece)

	soup = BeautifulSoup(html, "html.parser")
	title = soup.find(id='h1').text
	target = (
		'Responsabilidades e atribuições',
		'Requisitos e qualificações',
		'Diferenciais'
		)
	out = []
	# Para cada <div> no único elemento <section> da página.
	for outter_div in soup.section.contents:
		# Se houver um filho <h2> com título de interesse.
		if outter_div.h2.text in target:
			# Guarde o título e seu conteúdo subsequente.
			out.append(f"""### {outter_div.h2.text}\n{refine(str(outter_div.div))}\n""")
	return title.strip(), '\n'.join(out)

def get_page(url: str) -> str:
	"""
	Faz o download da página da vaga de emprego.
	"""
	response = requests.get(url)
	if response.status_code == 200:
		return response.text.replace('\u00A0', ' ')
	raise RuntimeError(f"Error downloading webpage: {response.status_code}")
