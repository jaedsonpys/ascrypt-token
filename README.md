# AScrypt tokens

O AScrypt é uma forma de gerar tokens de autenticação para sua aplicação de forma rápida e segura. Todos os
tokens que foram, mesmo que minimamente alterados, são inválidados imediatamente.

## Índice

* [Exemplos](#Exemplos)
    * [Tentando invalidar](#Tentando-invalidar)
    * [Chaves secretas](#Chaves-secretas)
* [Instalação](#Instalação)
* [Como usar](#Como-usar)
* [Licença](#Licença)

# Exemplos

Um token gerado utilizando o AScrypt tem a seguinte estrutura:

```
© AScrypt

66d03bda7ac0465c1291ce91e1f7e5f9.eyJuYW1lIjogIkphZWRzb24iLCAiQGVtaXRlZF9pbl9hc2NyeXB0IjogIjIwMjEtMTEtMjYgMjA6Mzg6MzguNDc0MTYyIn0=
```

O token é longo, mas vamos dividir ele através do ponto localizado no token. A primeira parte é um **hash md5** do conteúdo + a chave usada para a gerar o token. Veja o exemplo abaixo:

```python
© AScrypt

# transformando o dicionário em string
content_user = json.dumps({'name': 'Jaedson'})
secret_key = 'ogIkphZWRzb24iLCAiQGVta'

token_part1 = str(content_user + secret_key).encode()

hash_md5 = haslib.md5(token_part1).hexdigest()
# > 66d03bda7ac0465c1291ce91e1f7e5f9
```

Com isso, na hora de validar o token, nós geramos um hash do ***content*** e da ***chave secreta*** e comparamos o hash que veio no token e o hash que foi gerado na hora da validação.

Agora vamos para a segunda parte do token, que é nada mais que o conteúdo dele codificado em ***base64***. Um **token AScrypt** impede que o conteúdo seja alterado, garantindo a integridade da informação, porém, qualquer pessoa pode ver o conteúdo dele, mas não alterá-lo.

## Tentando invalidar

É praticamente impossível alterar esses tokens, mesmo que você altere o conteúdo do token e gere um novo hash, na hora de realizar a validação, o conteúdo será somado com a ***chave secreta***, que resulta em um hash totalmente diferente do que o usuário *mal intencionado* gerou.

## Chaves secretas

A classe ***AScrypt()*** possui um método que não precisa ser instanciado para uso, o **generate_token()** permite que token aleatórios sejam gerados para uso na codificação ou decodificação de tokens. Você pode especificar o tamanho da chave, sendo o padrão 32. Quanto maior a chave, mais seguro o token é.

# Licença

O AScrypt está licenciado por MIT.