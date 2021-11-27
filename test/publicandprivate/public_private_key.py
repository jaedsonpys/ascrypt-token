# usar chave privada para gerar tokens e chaves públicas para decodificar.
# o objetivo e manter a integridade do token. #

print('AScryptTest - Public and Private Keys')
print('-='*20)

import string
from random import choice
from base64 import b64encode, b64decode
from hashlib import md5

# test1

def token(private_key, content: dict):
    all_ = str(string.ascii_letters + string.digits + '@#$%&')
    len_key = 32

    public_key = ''.join([choice(all_) for __ in range(len_key)])

    # print('Public key:', public_key)
    # print('Private key:', private_key)

    content_token = f"{content}"
    base_content = b64encode(content_token.encode()).decode()
    # print('\nBase64 content:', base_content)
    # print('-='*20)


    # O token pode ser validado utilizando tanto a chave publica como
    # a chave privada, sem a necessidade de ter a chave privada em outro lugar.
    # 
    # Impedindo que tokens falsos sejam gerados utilizando a chave privada. #

    hash_private_key = md5(str(base_content + private_key).encode()).hexdigest()
    hash_public_key = md5(str(base_content + public_key).encode()).hexdigest()

    # print('\nPrivate Hash:', hash_private_key)
    # print('Public Hash:', hash_public_key)
    # print('-='*20)

    token = f'{hash_private_key}.{hash_public_key}.{base_content}'
    # print('\nResult token:', token)

    return (public_key, token)


def decode(public_key: str, token: str):
    division_token = token.split('.')
    __private_hash, public_hash, content_base = division_token

    test_hash = md5(str(content_base + public_key).encode()).hexdigest()
    return b64decode(content_base).decode() if test_hash == public_hash else False