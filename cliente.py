from socket import *
import ssl


def conectar_cliente():
    host = "localhost"
    porta = 12001

    caminho_certificado_cliente = "./ssl/certificado_cliente.crt"
    caminho_chave_cliente = "./ssl/chave_cliente.key"

    cliente = socket(AF_INET, SOCK_STREAM)
    cliente_ssl= ssl.wrap_socket(cliente, ca_certs="./ssl/certificado_cliente.crt")

    try:
        cliente_ssl.connect((host, porta))
        print("Conexão HTTPS segura estabelecida:")
        print(f"Protocolo: {cliente_ssl.version()}")
        print(f"Cifra: {cliente_ssl.cipher()}")

        while True:
            mensagem = input("Escreva sua mensagem: ")
            if mensagem:
                cliente_ssl.send(mensagem.encode())
    except Exception as e:
        print(f"Erro na conexão: {e}")
    finally:
        cliente_ssl.close()


if __name__ == "__main__":
    conectar_cliente()
