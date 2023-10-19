from socket import *



def iniciar_servidor():
    host = 'localhost'
    porta = 12001

    servidor = socket(AF_INET, SOCK_STREAM)
    servidor.bind((host, porta))
    servidor.listen(2)

    print("Servidor HTTPS está ouvindo em https://localhost:12001")

    while True:
        cliente_socket, endereco_cliente = servidor.accept()

        try:
            while cliente_socket:
                mensagem = cliente_socket.recv(1024)

                if mensagem:
                    print("Mensagem recebida do cliente: {mensagem.decode('utf-8')}")
        except Exception as e:
            print("Erro ao lidar com a mensagem: {e}")
        finally:
            cliente_socket.close()

if __name__ == "__main__":
    iniciar_servidor()
