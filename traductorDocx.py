#!/usr/bin/env python
# -*- coding: utf-8 -*-

from googletrans import Translator
from mtranslate import translate
import time
import sys
import docx

#translator = Translator()
archivoOrigen = ""
archivoDestino = ""

if sys.argv[1].endswith(".txt"):
	archivoOrigen = sys.argv[1]
	archivoDestino = archivoOrigen.split(".")[0] + "_trad.docx"
elif sys.argv[1] == "--help" or sys.argv[1] == "-h":
	print("El archivo a traducir se pasará al programa como primer argumento, debe ser un archivo con extensión .txt")
	sys.exit()
else:
	sys.exit()
f_dest = docx.Document()
f_src = open(archivoOrigen,encoding="utf8")

texto = f_src.read()

frases = texto.split(".")
indice = 0
for frase in frases:
	orig_para = f_dest.add_paragraph(str(frase)) 
	orig_para.style = 'Body Text 3' 
	#orig_para.add_run('\n')
	print(frase)
	intentos = 0
	while intentos < 10:
		try:
            #traduccion = translator.translate(frase,src='ru',dest='es')
			traduccion = translate(frase,"es","ru")
			#f_dest.write(traduccion.text)
			trad_para = f_dest.add_paragraph(traduccion)
			trad_para.style = 'Body Text 2' 
			#trad_para.add_run('\n')
			print(traduccion.encode("utf8"))
			intentos = 10
		except Exception as e:
			print(e)
			intentos += 1
			time.sleep(1)
	indice += 1
	#if indice % 2 == 0:
		#time.sleep(2)
	#elif indice % 15 == 0:
		#time.sleep(15)
print("Fin de la traduccion")
f_dest.save(archivoDestino)
f_src.close()
