import re
import requests

from bs4 import BeautifulSoup

def company_name(job_url):
	"""
	Extrai nome de empresa em URL de vaga na Gupy sob o formato:
		https://<empresa>.gupy.io/jobs/<id>?jobBoardSource=share_link
	"""
	return job_url[8:job_url.index('.gupy.')].capitalize()

def parse(html) -> tuple:
	"""
	Retorna empresa, título e descrição formatada da oferta de emprego de uma página Gupy.
	A função interna é útil para obter texto de bloco HTML respeitando novos parágrafos e itens de lista.
	"""
	def refine(piece):
		piece = piece.replace('<p', '\n<p').replace('<li', '\n- <li')
		return re.sub(r"<(.*?)>", '', piece)

	soup = BeautifulSoup(html, "html.parser")
	title = soup.find(id='h1').text
	out = []
	for outter_div in soup.section.contents:
		if outter_div.h2.text != 'INFORMAÇÕES ADICIONAIS':
			out.append(f"""#### {outter_div.h2.text}\n{refine(str(outter_div.div))}\n""")
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





