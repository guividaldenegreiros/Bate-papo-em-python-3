#!/usr/bin/python3

from socket import socket,AF_INET,SOCK_STREAM
from threading import Thread
 
#classe para manipular o socket
class Send:
 def __init__(self):
  self.__msg=''
  self.new=True
  self.con=None
 def put(self,msg):
  self.__msg=msg
  if self.con != None:
   #envia um mensagem atravez de uma conexão socket
   self.con.send(str.encode(self.__msg))
 def get(self):
  return self.__msg
 def loop(self):
  return self.new
 
#função esperar - Thread
def esperar(tcp,send,host='localhost',port=5000):
 destino=(host,port)
 #conecta a um servidor
 tcp.connect(destino)
  
 while send.loop():
  print('Conectado a ',host,'.')
  #atribui a conexão ao manipulador
  send.con=tcp
  while send.loop():
   #aceita uma mensagem
   msg=tcp.recv(1024)
   if not msg: break
   print(str(msg,'utf-8'))
 
if __name__ == '__main__':
 print('Digite o nome ou IP do servidor(localhost): ')
 host=input()
  
 if host=='':
  host = '127.0.0.1'
  
 #cria um socket
 tcp=socket(AF_INET,SOCK_STREAM)
 send=Send()
 #cria um Thread e usa a função esperar com dois argumentos
 processo=Thread(target=esperar,args=(tcp,send,host))
 processo.start()
 print('')
  
 msg=input("antes de enviar uma mensagem, por favor informe seu nome!\n")
 while True:
  send.put(msg)
  msg=input()
  
 processo.join()
 tcp.close()
 exit()
