from hashlib import md5
import json
import string
from random import choice
from base64 import b64encode, b64decode
from datetime import date, datetime

class AScrypt:
    def __init__(self, key: str=None):
        """Prepara o AScrypt para manipulação
        de tokens.

        Args:
            key (str): Chave a ser usada para codificar
            e decodificar os tokens.
        """

        if not key:
            raise ValueError('O argumento "key" deve ser em string.')

        self.key = key

    def new_token(self, content: dict=None) -> str:
        """Gera um novo token.

        Args:
            content (dict, optional): JSON que vai
            no corpo do seu token, podendo ser acessado
            após a decodificação. O padrão é None e uma
            exceção é lançada se nenhum content for passado.

        Raises:
            ValueError: Caso nenhum content for definido.

        Returns:
            str: Token que foi criado.
        """

        if not content:
            raise ValueError('Um content é necessário para gerar tokens.')

        # A chave @emited_in_ascrypt é uma forma de deixar
        # o token mais seguro, fazendo que um token criado com o
        # dicionário de outro token seja diferente. #

        content['@emited_in_ascrypt'] = str(datetime.now())

        # generate hash for content + key
        hash_content = md5(str(json.dumps(content) + self.key).encode()).hexdigest()

        # base64 enconde content
        encoded_content = b64encode(json.dumps(content).encode()).decode()

        token = '{hc}.{ec}'.format(ec=encoded_content, hc=hash_content)
        return token


    # ! public methods ! #

    def generate_key(len: int=32) -> str:
        """Essa função gera uma chave aleatória para
        ser usada na codificação e decodificação de tokens.

        Args:
            len (int, optional): Tamanho da chave. Quanto maior
            ela for, mais será segura. O padrão é 32.

        Returns:
            str: Retorna a chave em formato de string.
        """

        ascii_letters = string.ascii_letters
        chars = '@$&#?!'
        numbers = string.digits

        all = ascii_letters + numbers + chars

        key = ''.join([choice(all) for __ in range(len)])
        return key

mykey = AScrypt.generate_key(5024)
asc = AScrypt(mykey)

token = asc.new_token({'sender': 'Jaedson'})
print(token)