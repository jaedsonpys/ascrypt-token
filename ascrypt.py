from hashlib import md5
import json
import string
from random import choice
from base64 import b64encode, b64decode
from datetime import datetime
import exceptions


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

    def new_token(self, content: dict) -> str:
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

        if not content or not isinstance(content, dict):
            raise ValueError('Um content em formato de dicionário é necessário para gerar tokens.')

        # A chave @emited_in_ascrypt é uma forma de deixar
        # o token mais seguro, fazendo que um token criado com o
        # dicionário de outro token seja diferente. #

        content['@emited_in_ascrypt'] = str(datetime.now())

        # base64 enconde content
        encoded_content = b64encode(json.dumps(content).encode()).decode()

        # generate hash for content + key
        hash_content = md5(str(encoded_content + self.key).encode()).hexdigest()

        token = '{hc}.{ec}'.format(ec=encoded_content, hc=hash_content)
        return token

    def decode_token(self, token: str):
        division_token = token.split('.')

        if not len(division_token) == 2:
            raise exceptions.InvalidTypeToken()

        # informações necessárias para validar o token
        hash_token, content_token = division_token

        # gerando hash para validar o token
        test_hash_token = md5(str(content_token + self.key).encode()).hexdigest()

        token_is_valid = True if test_hash_token == hash_token else False
        if token_is_valid:
            return json.loads(b64decode(content_token))
        else:
            # o token é inválido
            raise exceptions.InvalidToken()

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
        