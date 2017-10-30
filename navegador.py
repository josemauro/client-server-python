# -*- coding: utf-8 -*-
# Trabalho de Redes de computadores #
#  		  Jose Mauro Ribeiro		#

import sys
import socket
import os

PORT = 80 		#porta que servidor esta

def parser_parametros(parametros):
	
	#checa se o protocolo foi especificado (http ou ftp)
	if (':' in parametros[1] ):
		parametros[1] = parametros[1].split('://')
	else:
		parametros[1] = ['http', parametros[1]]
	return parametros
	

print "Executando cliente...\n"

num_param = len(sys.argv) #num de parametros passados para o cliente

if num_param == 1:
    print "Execute o navegador informando a url (obrigatorio) e a porta (opcional)!"
    sys.exit()
    
if num_param == 3:
	PORT = int(sys.argv[2])

parametros = parser_parametros(sys.argv)

HOST = parametros[1][1].split('/')
HOST = HOST[0]

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect((HOST, PORT))

msg = sys.argv[1]

url = parametros[1][1].split('/')
del url[0]
caminho_do_arquivo = ''

if type(url) == list:
	for i in url:
		caminho_do_arquivo += '/'+i
else:
	caminho_do_arquivo = '/'

if (parametros[1][0] == 'http'):
	mensagem = 'GET '+caminho_do_arquivo+' HTTP/1.0\r\nUser-Agent: Mozilla/4.0 (compatible; MSIE5.01; Windows NT)\r\nHost: '+HOST+'\r\n\r\n'
	tcp.sendall(mensagem)

arquivo_saida = open("site_buscado.html","w")
pagina = ''

while (True):
	rcv = tcp.recv(4096)
	if not rcv:
		break
	pagina += rcv
arquivo_saida.write(pagina)
tcp.close
