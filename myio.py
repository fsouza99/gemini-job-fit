from datetime import datetime
from string import Template

from settings import PROMPTFILE

def curr_date() -> str:
	return str(datetime.today().date())

def write_file(path, text, footnote=None) -> None:
	with open(path, 'w', encoding='utf8') as file:
		file.write(text)
		if footnote is not None:
			file.write(f'\n\n---\n{footnote}')
	return

def read_file(path) -> str:
	with open(path, encoding='utf8') as file:
		text = file.read()
	return text

def set_prompt(job_position, job_description, curriculum) -> str:
	"""
	Constrói prompt a partir de modelo em arquivo.
	"""
	return Template(read_file(PROMPTFILE)).substitute(
			job_position=job_position.lower(),
			job_description=job_description,
			curriculum=curriculum)