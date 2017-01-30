#coding: utf-8
'''
Renombra archivos de la forma
año-nombre
a la forma
nombre (año)
Pensado para archivos de música
'''

from six.moves import input #compatibilidad 2/3

import os
import re

def rename(string):
	expr = r'''
	[- _()]* #separador
	(\d{4})  #año
	[- _()]* #separador
	(.+)     #nombre
	'''

	match = re.findall(expr, string, re.VERBOSE)

	if match != []:
		(a, n) = match[0]
		return n + " (" + a + ")"
	else:
		return string

uso = '''
Este programa renombra archivos y directorios de la forma
'año nombre' a la forma 'nombre (año)'
Ejemplo: '1989 The Cure - Disintegration' a 'The Cure - Disintegration (1989)'
'''
menu = '''
[1] Cambiar directorio
[2] Ver archivos del directorio actual
[3] Renombrar archivos

[4] Salir del programa

'''

def main():
	print(uso)
	valid_inputs = ["1","2","3","4"]
	while 1:
		print(menu)
		print("Directorio actual: " + os.getcwd())
		
		option = input(">")
		while option not in valid_inputs:
			print("Opción no válida")
			option = input(">")
		if   option == "1":
			changedir()
		elif option == "2":
			printfiles()
		elif option == "3":
			renamefiles()
		elif option == "4":
			return

def changedir():
	newdir = input("Nuevo directorio: ")
	if os.path.exists(newdir):
		os.chdir(newdir)
	else:
		print(newdir + " no existe")

def printfiles():
	files = os.listdir(os.getcwd())
	for file in files:
		print(file[:35] + " a " + rename(file)[-35:])

def renamefiles():
	files = os.listdir(os.getcwd())
	for file in files:
		os.rename(file,rename(file))

if __name__ == '__main__':
	main()
