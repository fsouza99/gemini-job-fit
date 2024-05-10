from sys import argv

from bot import Bot
from miscellaneous import *
from myio import *
from scraper import *
from settings import *

if set_environment():
	print(HELP_MSG1)
	exit(0)

if len(argv) < 2:
	print(HELP_MSG2)
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
	prefix = f'{OUTPUTDIR}\\{fix_title(company_name)} - {fix_title(job_position)}'
	curr_date = curr_date()
	write_file(f'{prefix} (prompt).md', prompt, curr_date)
	write_file(f'{prefix} (response).md', response, curr_date)
