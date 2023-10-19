# ServidorClienteSocketHTTPsSeguro
Aplicar  SSL/TLS com certificado gerado por uma Autoridade Certificadora criada, em um Servidor HTTPS desenvolvido por socket

## Porque usar SSL?
adição de SSL, arquivos de chave e certificado a um socket é uma melhoria significativa para a segurança da comunicação, tornando-a apropriada para aplicativos que exigem proteção de dados sensíveis e conformidade com padrões de segurança. Isso ajuda a garantir a confidencialidade, integridade e autenticidade dos dados transmitidos.

## Como gerar a chave e o certificado SSL?
Eu utilizei o WSL que é um subsistema Linux dentro do Sistema Operacional Windows. E precisei da biblioteca de código aberto OpenSSL, que é utilizada para  criptografia, segurança e autenticação em aplicativos de software e sistemas. Ele oferece uma ampla gama de recursos de criptografia e é amplamente adotado em várias aplicações e sistemas operacionais.

Com os seguintes passos:

1. No terminal de comando eu instalei o openssl:
```sudo apt-get install openssl```

2. Após instalar o openssl, foi executado o comando que gera uma chave privada utilizando o algoritmo de criptografia RSA:
```openssl genpkey -algorithm RSA -out chave.key```

3. Gerar um arquivo solicitação de certificado (CSR), associando a chave privada gerada anteriormente, e incluindo informações como nome comum (CN), organização, etc. 
```openssl req -new -key chave.key -out solicitacao.csr```

4. Gere um certificado autoassinado, pegando o CSR, assinando o CSR com a chave privada especificada e gerando um certificado digital autoassinado. Que pode ser usado para criar conexões seguras, como em um servidor web, mas não é amplamente confiável por padrão, pois não foi emitido por uma Autoridade de Certificação confiável. Em vez disso, é frequentemente usado para fins de desenvolvimento, testes e ambientes internos.

```openssl x509 -req -days 365 -in sua_solicitacao.csr -signkey chave.key -out certificado.crt```
