from abc import ABC, abstractmethod
from persistencia.dao import DAO
from entidade.cliente import Cliente

class ClienteDAO(DAO):
    def __init__(self):
        super().__init__('clientes.pkl')

    def add(self, cliente: Cliente):
        if (isinstance(cliente.codigo, int)) and (cliente is not None) and isinstance(cliente, Cliente):
            super().add(cliente.codigo, cliente)

    def get(self, key: int):
        if super().valida_chave_int(key):
            return super().get(key)

    def remove(self, key: int):
        if super().valida_chave_int(key):
            return super().remove(key)
