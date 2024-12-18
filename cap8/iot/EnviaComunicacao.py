import serial
from serial.tools import list_ports

#lista de portas no arduino
for port in list_ports.comports():
    print('Dispositivo: {} - porta: {}'.format(port.description, port.device))

#configuração da porta arduino
conexao = serial.Serial('COM3', 115200)

acao = input("Digite a acao: "
             "\n<L> - ligar"
             "\n<D> - desligar")

while acao == "L" or acao == "D":
    if acao == "L":
        conexao.write(b'1')
    elif acao == "D":
        conexao.write(b'0')

    acao = input("Digite a acao: "
                 "\n<L> - ligar"
                 "\n<D> - desligar")

conexao.close()
print("conexao encerrada")
