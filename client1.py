import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
lista = ['VetorA', '1', '2', '3', '4', '5', 'break']

while True:
    for i in range(len(lista)):
        valor = lista[i]
        mensagem_envio = valor
        cliente.sendto(mensagem_envio.encode(), ("localhost", 33000))
        mensagem_bytes, endereco_ip_servidor = cliente.recvfrom(2048)

    break