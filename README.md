### Prova de Sistema Distribuido

<hr>

#### Para conseguir executar esse sistema em seu computador você deve:

- Ter o Python na versão 3.5 ou superior
- Ter o Pip na versão 8
- Ter o Mosquitto instalado na sua máquina

#### Dependências 

Antes de executar o programa você deve instalar a depedência paho-mqtt. <br> 
Dentro da pasta do seu projeto execute o seguinte comando

> pip install paho-mqtt

#### Ordem de execução 

Para garantir que o programa execute corretamente, você precisa seguir uma ordem de iniciação dos processos

1. python3 calc_serve.py
2. python3 serv.py
3. python3 processoB.py
4. python3 processoA.py