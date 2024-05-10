import os

def write_file(path, text, footnote=None) -> None:
	with open(path, 'w', encoding='utf8') as file:
		file.write(text)
		if footnote is not None:
			file.write(f'\n\n---\n\n{footnote}')
	return

def read_file(path) -> str:
	with open(path, encoding='utf8') as file:
		text = file.read()
	return text

def set_environment() -> bool:
	"""
	Se necessário, cria as dependências da execução principal.
	Retorna booleano que informa se algum elemento foi criado, isto é,
	se a working tree foi alterada.
	"""
	target_dir = os.listdir("files")
	altered_wt = False

	if not "output" in target_dir:
		os.mkdir("files\\output")
		print("Diretório criado: files\\output")
		altered_wt = True

	if not "apikey" in target_dir:
		with open("files\\apikey", 'w') as file:
			file.write("GEMINI_API_KEY=Chave")
		print("Arquivo criado: files\\apikey")
		altered_wt = True

	if not "curriculum.md" in target_dir:
		open("files\\curriculum.md", 'w').close()
		print("Arquivo criado: files\\curriculum.md")
		altered_wt = True

	return altered_wt