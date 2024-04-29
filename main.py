"""
Avisos

1. Execute set_env.py para criação de dependências.
2. Passe a URL da página de uma vaga no portal Gupy como argumento a este programa.
3. Registre uma chave de acesso ao Gemini em files/apikey.
4. Salve o currículo a ser avaliado em files/curriculum.md.
5. O prompt a ser enviado será construído conforme template em files/prompt_model.
"""

from bot import Bot
from myio import *
from scraper import *
from settings import *

from sys import argv

if len(argv) < 2:
	print(HELP_MSG)
	exit(1)

print('Realizando download da página.')
company_name = company_name(argv[1])
job_page = get_page(argv[1])

print('Extraindo informações da vaga de emprego.')
job_position, job_desc = parse(job_page)

print('Construindo prompt.')
curriculum = read_file(CVFILE)
prompt = set_prompt(job_position, job_desc, curriculum)

print('Comunicando o Gemini.')
gproxy = Bot()
response = gproxy.send_prompt(prompt)
print('Comunicação encerrada.')

if response is None:
	print('Falha na comunicação.')
else:
	print('Salvando informações.')
	prefix = f'{OUTPUTDIR}\\{company_name} - {job_position}'
	curr_date = curr_date()
	write_file(f'{prefix} (prompt).md', prompt, curr_date)
	write_file(f'{prefix} (response).md', response, curr_date)









