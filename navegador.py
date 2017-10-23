# -*- coding: utf-8 -*-

import sys
import socket
import os


HOST = 'localhost'  #endereco de ip do servidor
PORT = 80 		#porta que servidor esta

print "Executando cliente...\n"

num_param = len(sys.argv) #num de parametros passados para o cliente

if num_param == 1:
    print "Execute o navegador informando a url (obrigatorio) e a porta (opcional)!"
    sys.exit()
if num_param == 3:
	PORT = int(sys.argv[2])

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect((HOST, PORT))
print 'Para sair digite CTRL+X\n'

msg = sys.argv[1]

while (msg != '\x18'):
    tcp.send(msg)
    print tcp.recv(4096)+"\nfim do arquivo"
    msg = raw_input()
    
tcp.close
