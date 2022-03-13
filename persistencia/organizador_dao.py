from persistencia.abstract_dao import DAO
from entidade.organizador import Organizador

class OrganizadorDAO(DAO):

    def __init__(self):
        super().__init__('organizador.pkl')

    def add(self, organizador: Organizador):
        if self.__organizador_valido(organizador):
            super().add(organizador.id_organizador, organizador)

    def remove(self, organizador: Organizador):
        if self.__organizador_valido(organizador):
            super().remove(organizador.id_organizador)

    def __organizador_valido(self, organizador):
        return (organizador is not None) and (isinstance(organizador, Organizador)) and (isinstance(organizador.id_organizador, int))