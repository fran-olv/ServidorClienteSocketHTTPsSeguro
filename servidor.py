from socket import *
import ssl


def iniciar_servidor():
    host = "localhost"
    porta = 12001

    caminho_certificado= ".ssl/certificado_servidor.crt"
    caminho_chave=".ssl/chave_servidor.key"

    servidor = socket(AF_INET, SOCK_STREAM)
    servidor.bind((host, porta))
    servidor.listen(2)

    print("Servidor de pé! ")

    while True:
        cliente_socket, endereco_cliente = servidor.accept()

        servidor_ssl = ssl.wrap_socket(
            cliente_socket,
            server_side=True,
            certfile="./ssl/certificado_servidor.crt",
            keyfile="./ssl/chave_servidor.key",
            ssl_version= ssl.PROTOCOL_TLSv1
        )



        try:
            print("Conexão segura estabelecida:")
            print(f"Protocolo: {servidor_ssl.version()}")
            print(f"Cifra: {servidor_ssl.cipher()}")

            while servidor_ssl:
                mensagem = servidor_ssl.read()
                if mensagem:
                    print(f"Mensagem recebida do cliente: {mensagem.decode('utf-8')}")

        except ssl.SSLError as e:
            print(f"Erro SSL: {e}")
        except Exception as e:
            print(f"Erro ao lidar com a mensagem: {e}")
        finally:
            servidor_ssl.close()
            cliente_socket.close()

if __name__ == "__main__":
    iniciar_servidor()
