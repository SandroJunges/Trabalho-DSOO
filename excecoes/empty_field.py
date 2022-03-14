class EmptyFieldError(Exception):
    def __init__(self, mensagem = "Preencha todos os campos") -> None:
        self.mensagem = mensagem
        super().__init__(mensagem)