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
    
    if (msg == "break"):
        break
    else:
        lista.append(msg)


for i in range(len(lista)):
    val = lista[i]
    if ('x' in val):
        listaA.append(val)
    else:
        listaB.append(val)


print(listaA)
print("-----------------------")
print(listaB)