import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

servidor.bind(("", 33000))

lista = []
listaA = []
listaB = []

while True:
    mensagem_bytes, endereco_ip_cliente = servidor.recvfrom(2048)

    mensagem_resposta = mensagem_bytes.decode()

    servidor.sendto(mensagem_resposta.encode(), endereco_ip_cliente)

    msg = mensagem_resposta
    
    if (msg == "xbreak"):
        break
    else:
        lista.append(msg)


for i in range(len(lista)):
    if "x" in lista[i]:
        listaA.append(lista[i])
    else:
        listaB.append(lista[i])


print("Tamanho da lista A:", len(listaA))
print(listaA)

print(" ")
print(" ")
print(" ")

print("Tamanho da Lista B:", len(listaB))
print(listaB)

tamanhoTotal = len(listaA) + len(listaB)

print(" ")
print(" ")
print(" ")

print('Tamanho total: ', tamanhoTotal)