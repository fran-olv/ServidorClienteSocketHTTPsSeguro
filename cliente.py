from socket import *


def conectar_cliente():
    host = 'localhost'
    porta = 12001


    cliente = socket(AF_INET, SOCK_STREAM)
    cliente.connect((host,porta))

    while True:
        mensagem = input("Escreva sua mensagem:> ")

        if mensagem:
            cliente.send(mensagem.encode())

    clinte.close()

if __name__ == "__main__":
    conectar_cliente()
