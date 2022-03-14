class SaldoIndisponivelException(Exception):
    def __init__(self):
        super().__init__("O valor é superior ao saldo disponivel para realização da operação!")