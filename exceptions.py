class Error(Exception):
    pass

class InvalidTypeToken(Error):
    def __init__(self):
        """Exceção lançada quando o formato do token é inválido"""

        self.expression = 'InvalidTypeToken'
        self.message = 'O token disponibilizado não é válido.'

class InvalidToken(Error):
    def __init__(self):
        """Exceção lançada quando o token foi modificado ou a chave não
        é válida"""

        self.expression = 'InvalidToken'
        self.message = 'O token foi alterado ou a chave não é válida.'