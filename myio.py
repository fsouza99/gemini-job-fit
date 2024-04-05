from settings import PROMPT_PATH
from string import Template

def write_file(path, text) -> None:
	"""
	Salva texto em arquivo.
	"""
	with open(path, 'w', encoding='utf8') as file:
		file.write(text)
	return

def read_file(path) -> str:
	"""
	Extrai o texto de um arquivo.
	"""
	with open(path, encoding='utf8') as file:
		text = file.read()
	return text

def set_prompt(job_pos, job_desc, candidate_cv) -> str:
	"""
	Constrói prompt a partir de modelo em arquivo.
	"""
	return Template(read_file(PROMPT_PATH)).substitute(
		position=job_pos, job_description=job_desc, curriculum=candidate_cv)