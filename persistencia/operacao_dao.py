from abc import ABC, abstractmethod
from persistencia.dao import DAO
from entidade.operacao import Operacao

class OperacaoDAO(DAO):
    def __init__(self):
        super().__init__('operacoes.pkl')

    def add(self, operacao: Operacao):
        if (isinstance(operacao.codigo, int)) and (operacao is not None) and isinstance(operacao, Operacao):
            super().add(operacao.codigo, operacao)

    def get(self, key: int):
        if super().valida_chave_int(key):
            return super().get(key)

    def remove(self, key: int):
        if super().valida_chave_int(key):
            return super().remove(key)