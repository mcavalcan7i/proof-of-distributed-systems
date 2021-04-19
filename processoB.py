import paho.mqtt.client as mqtt
import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

listaB = " "
teste = []


def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        client.subscribe ("vetorB")
        client.subscribe ("operacaoB")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg): 
    listaB = msg.topic+" >>> "+str(msg.payload)
    teste.append(listaB)

    if (len(teste) >= 2):
        client.disconnect()

if __name__ == '__main__':
    client = mqtt.Client()
    client.connect ("localhost", 1883, 60)
    client.on_connect = on_connect
    client.on_message = on_message
    client.loop_forever()

arrayB = []
operacaoB = []

for i in range(len(teste[0])):
    if (teste[0][i].isdigit()):
        arrayB.append(teste[0][i])

for i in range(len(teste[1])): #16 17
    if (i == 16 or i == 17):
        operacaoB.append(teste[1][i])

print(arrayB)
print("-----------------")
print(operacaoB)


for i in range(len(arrayB)):
    if (arrayB[i] != 'VetorB'):
        arrayB[i] = int(arrayB[i])

operacaoB[1] = int(operacaoB[1])

if (operacaoB[0] == "+"):
    for i in range(len(arrayB)):
        if (arrayB[i] != "VetorB"):
            arrayB[i] += operacaoB[1]
elif (operacaoB[0] == "-"):
    for i in range(len(arrayB)):
        if (arrayB[i] != "VetorB"):
            arrayB[i] -= operacaoB[1]
elif (operacaoB[0] == "*"):
    for i in range(len(arrayB)):
        if (arrayB[i] != "VetorB"):
            arrayB[i] *= operacaoB[1]
elif (operacaoB[0] == "/"):
    for i in range(len(arrayB)):
        if (arrayB[i] != "VetorB"):
            arrayB[i] /= operacaoB[1]
elif (operacaoB[0] == "^"):
    for i in range(len(arrayB)):
        if (arrayB[i] != "VetorB"):
            arrayB[i] = (arrayB[i] ** operacaoB[1])


print(arrayB)
print("-----------------")
print(len(arrayB))

arrayB.append("break")

while True:
    for i in range(len(arrayB)):
        valor = str(arrayB[i])
        mensagem_envio = valor
        cliente.sendto(mensagem_envio.encode(), ("localhost", 33000))
        mensagem_bytes, endereco_ip_servidor = cliente.recvfrom(2048)

    break