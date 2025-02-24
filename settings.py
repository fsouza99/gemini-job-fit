# Modelo do Gemini a ser usado.
MODEL_NAME = 'gemini-1.5-pro'

# Caminho para arquivo com chave de acesso à Gemini API.
# Ao editar o arquivo, mantenha o formato GEMINI_API_KEY=Chave.
API_KEY_PATH = "files\\apikey"

# Caminho para arquivo com descrição do currículo.
# É aconselhável que esteja no formato dos currículos da Gupy.
CVFILE = "files\\curriculum.md"

# Caminho para arquivo com modelo de prompt.
PROMPTFILE = "files\\prompt_model.md"

# Caminho para diretório de prompts enviados e respostas do Gemini.
OUTPUTDIR = 'files\\output'

# Mensagens de ajuda.
HELP_MSG1 = f"""Dependências geradas no diretório "files".
Execute novamente para obter ajuda."""
HELP_MSG2 = f"""Comando: py main.py <gupy_url> [-p].

Orientações:

	- O currículo deve estar escrito em "files/curriculum.md", aconselhavelmente
	fazendo uso da sintaxe Markdown para aprimorar o entendimento do Gemini
	sobre a entrada (veja o exemplo em "files").
	- O prompt será construído conforme o template em "files/prompt_model.md".
	- Para consultar o Gemini, é necessário fornecer uma chave de acesso no
	arquivo "files/apikey".

Parâmetros:

	{"gupy_url":<10}\tEndereço web da vaga na Gupy.
	{"-p":<10}\tApenas gera o prompt e finaliza.
"""
