"""
Avisos

1. Passe a URL da página de uma vaga no portal Gupy como argumento a este programa.
2. Registre uma chave de acesso ao Gemini em files/apikey.
3. Salve o currículo a ser avaliado em files/curriculum.txt.
4. O prompt a ser enviado será construído conforme template em files/prompt_model.
5. Verifique o arquivo settings.py antes de executar.
"""

from scraper import *
from bot import Bot
from myio import *
from settings import CVFILE, HELP_MSG
from sys import argv

if len(argv) < 2:
	print(HELP_MSG)
	exit(1)

print('Realizando download da página.')
job_url = argv[1]
job_page = get_page(job_url)

print('Extraindo informações da vaga de emprego.')
job_title, job_desc = parse(job_page)

print('Obtendo currículo.')
curriculum = read_file(CVFILE)

print('Construindo prompt.')
prompt = set_prompt(job_title, job_desc, curriculum)

print('Comunicando o Gemini.')
gproxy = Bot()
response = gproxy.send_prompt(prompt)
print('Comunicação encerrada.')

if response is None:
	print('Falha na comunicação.')
else:
	print('Salvando informações.')
	write_file(path=f'{job_title} (description).txt', text=job_desc)
	write_file(path=f'{job_title} (prompt).txt', text=prompt)
	write_file(path=f'{job_title} (response).md', text=response)




