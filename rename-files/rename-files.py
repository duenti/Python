import os

def rename_file():
	#1) Recuperar todos arquivos da pasta
	dir = os.getcwd() + '/images2'
	file_list = os.listdir(dir)
	for file in file_list:
		new_name = ''
		file2 = dir + '/' + file
		for c in file:
			if not c.isdigit():
				new_name += c
		new_file2 = dir + '/' + new_name
		os.rename(file2,new_file2)

rename_file()

#Para remover os numeros de uma string tambem pode usar:
#file_name.translate(None,"0123456789")