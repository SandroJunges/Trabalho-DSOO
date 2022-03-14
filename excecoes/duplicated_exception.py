class DuplicatedException(Exception):
    def __init__(self, mensagem_personalizada: str = None):
        super().__init__(mensagem_personalizada)