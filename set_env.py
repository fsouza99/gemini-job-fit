import os

target_dir = os.listdir("files")

if not "output" in target_dir:
	os.mkdir("files\\output")
	print("files\\output folder created.")

if not "apikey" in target_dir:
	with open("files\\apikey", 'w') as file:
		file.write("GEMINI_API_KEY=chave")
	print("files\\apikey file created.")

if not "curriculum.md" in target_dir:
	open("files\\curriculum.md", 'w').close()
	print("files\\curriculum.md file created.")

