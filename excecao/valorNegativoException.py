class ValorNegativoException(Exception):
    def __init__(self):
        super().__init__("O valor da operação é negativo ou superior ao saldo disponivel para realização da operação!")