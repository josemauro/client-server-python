# -*- coding: utf-8 -*-

# Trabalho de Redes de computadores #
#  		  Jose Mauro Ribeiro		#

import socket
import thread
import sys
import os

if len(sys.argv) == 1:
	print "Warning: nenhuma pasta de arquivos foi passada como parametro!!\n"

PASTA_DE_ARQUIVOS = sys.argv[1]

def existe_arquivo(arquivo):
	caminho = PASTA_DE_ARQUIVOS + '/' + arquivo
	return os.path.isfile(caminho)
	
def conectado(con, cliente):
	print "Conenectado ao cliente ", cliente
	
	while True:
		mensagem = con.recv(1024)
		if existe_arquivo(mensagem):
			f = open(PASTA_DE_ARQUIVOS + '/' +mensagem)
			arquivo = f.read()
			con.sendall(arquivo)
		else:
			con.send("Erro 404 - Arquivo nao encontrado")
	print "Fechando conexao com o cliente ", cliente
	con.close()

HOST = 'localhost' 		# endereco ip do servidor
PORT = 5000 			# porta que o servidor esta

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.bind((HOST, PORT)) 	# associa o socket a uma porta e um IP
tcp.listen(1)			# coloca o servidor escutando (modo passivo)

while True:
	con, cliente = tcp.accept() # retorna um objeto socket novo e o endereço do cliente
	thread.start_new_thread(conectado, tuple([con, cliente]))
tcp.close()
