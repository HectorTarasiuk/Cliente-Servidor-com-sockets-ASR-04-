from socket import *
from constCS import *  # -
 
s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))  # connect to server (block until accepted)
print("Conectado ao servidor.")
print("Operações disponíveis:")
print("  overhang;<valor>   -> ex: overhang;10")
print("  prime;<numero>     -> ex: prime;104729")
print("  wordfreq;<texto>   -> ex: wordfreq;o rato roeu a roupa do rei de roma")
print("Digite 'sair' para encerrar.\n")
 
while True:
    msg = input("Requisição > ")
    if msg.strip().lower() == "sair":
        break
    s.send(str.encode(msg))       # send the chosen operation + dados
    data = s.recv(1024)           # receive the response
    print("Resposta:", bytes.decode(data))  # print the result
 
s.close()  # close the connection
 
