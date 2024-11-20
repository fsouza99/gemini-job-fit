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
Antes de executar novamente, informe as entradas nos arquivos criados."""
HELP_MSG2 = "Comando: py main.py <gupy_url>"
