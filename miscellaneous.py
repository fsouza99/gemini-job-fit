import re

from datetime import datetime
from string import Template

from myio import read_file
from settings import PROMPTFILE

def company_name(job_url) -> str:
	"""
	Extrai nome de empresa em URL de vaga na Gupy sob o formato:
		https://<empresa>.gupy.io/jobs/<id>?jobBoardSource=share_link
	"""
	return job_url[8:job_url.index('.gupy.')].capitalize()

def curr_date() -> str:
	return str(datetime.today().date())

def fix_title(filename) -> str:
	"""
	Remove de um texto caracteres proibidos em nomes de arquivos.
	"""
	return re.sub(r'[\\/:*?<>|"]', '-', filename)
	
def set_prompt(job_position, job_description, curriculum) -> str:
	"""
	Constrói prompt a partir de modelo em arquivo.
	"""
	return Template(read_file(PROMPTFILE)).substitute(
			job_position=job_position.lower(),
			job_description=job_description,
			curriculum=curriculum)
