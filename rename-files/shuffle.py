import os
import random

def shuffle():
	#1) Recuperar todos arquivos da pasta
	dir = os.getcwd() + '/images2'
	file_list = os.listdir(dir)
	for file in file_list:
		new_name = ''
		d1 = random.randint(0,9)
		d2 = random.randint(0,9)
		new_name = str(d1) + str(d2) + file
		file2 = dir + '/' + file
		
		new_file2 = dir + '/' + new_name
		print(new_file2 + '\n')
		os.rename(file2,new_file2)

shuffle()

#Para remover os numeros de uma string tambem pode usar:
#file_name.translate(None,"0123456789")