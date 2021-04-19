import paho.mqtt.client as mqtt
import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


listaA = " "
teste = []


def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        client.subscribe ("vetorA")
        client.subscribe ("operacaoA")
        client.publish ("novaOperacao", "start")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg): 
    listaA = msg.topic+" >>> "+str(msg.payload)
    teste.append(listaA)

    if (len(teste) >= 2):
        client.disconnect()

if __name__ == '__main__':
    client = mqtt.Client()
    client.connect ("localhost", 1883, 60)
    client.on_connect = on_connect
    client.on_message = on_message
    client.loop_forever()

arrayA = []
operacaoA = []

for i in range(len(teste[0])):
    if (teste[0][i].isdigit()):
        arrayA.append(teste[0][i])

for i in range(len(teste[1])): #16 17
    if (i == 16 or i == 17):
        operacaoA.append(teste[1][i])


# print("espaco")


print(arrayA)
print("-----------------")
print(operacaoA)

print("-----------------")


for i in range(len(arrayA)):
    if (arrayA[i] != 'VetorA'):
        arrayA[i] = int(arrayA[i])

operacaoA[1] = int(operacaoA[1])

if (operacaoA[0] == "+"):
    for i in range(len(arrayA)):
        if (arrayA[i] != 'VetorA'):
            arrayA[i] += operacaoA[1]
elif (operacaoA[0] == "-"):
    for i in range(len(arrayA)):
        if (arrayA[i] != 'VetorA'):
            arrayA[i] -= operacaoA[1]
elif (operacaoA[0] == "*"):
    for i in range(len(arrayA)):
        if (arrayA[i] != 'VetorA'):
            arrayA[i] *= operacaoA[1]
elif (operacaoA[0] == "/"):
    for i in range(len(arrayA)):
        if (arrayA[i] != 'VetorA'):
            arrayA[i] /= operacaoA[1]
elif (operacaoA[0] == "^"):
    for i in range(len(arrayA)):
        if (arrayA[i] != 'VetorA'):
            arrayA[i] = (arrayA[i] ** operacaoA[1])

for i in range(len(arrayA)):
    arrayA[i] = "x" + str(arrayA[i])

print(arrayA)
print("-----------------")
print(len(arrayA))

while True:
    for i in range(len(arrayA)):
        mensagem_envio = arrayA[i]
        cliente.sendto(mensagem_envio.encode(), ("localhost", 33000))
        mensagem_bytes, endereco_ip_servidor = cliente.recvfrom(2048)

    break