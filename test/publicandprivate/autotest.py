from public_private_key import token, decode
from random import choice, randint
import string

len_key = 32

# O objetivo deste teste é gerar tokens
# com diferentes informações com chaves
# privadas aleatórias.
# 
# Após isso, tentar quebrar a chave
# privada gerar tokens falsos. #

class Test:
    def __init__(self, repetions: int):
        self.repetions = repetions

    def start(self):
        generate_tokens = []

        # gerando tokens
        for __ in range(self.repetions):
            all_ = str(string.ascii_letters + string.digits + '@#$%&')
            aleatory_private_key = ''.join([choice(all_) for __ in range(len_key)])

            keys = ['name', 'email', 'state', 'country', 'random']
            values = ['Jaedson', 'test@python.org', 'Unknow', 'Brazil', randint(10000, 99999)]

            content = dict([(k,v) for k,v in zip(keys, values)])

            public_key, new_token = token(aleatory_private_key, content)
            generate_tokens.append((new_token, public_key, aleatory_private_key))
            

        for tk, pck, pvk in generate_tokens:
            print(tk, pck, pvk)
            print()


a = Test(10)
a.start()