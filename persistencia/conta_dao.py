from abc import ABC, abstractmethod
from persistencia.dao import DAO
from entidade.conta import Conta

class ContaDAO(DAO):
    def __init__(self):
        super().__init__('contas.pkl')

    def add(self, conta: Conta):
        if (isinstance(conta.codigo, int)) and (conta is not None) and isinstance(conta, Conta):
            super().add(conta.codigo, conta)

    def get(self, key: int):
        if super().valida_chave_int(key):
            return super().get(key)

    def remove(self, key: int):
        if super().valida_chave_int(key):
            return super().remove(key)
