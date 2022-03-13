from persistencia.abstract_dao import DAO
from entidade.competicao import Competicao

class CompeticaoDAO(DAO):

    def __init__(self):
        super().__init__('competicao.pkl')

    def add(self, competicao: Competicao):
        if self.__competicao_valida(competicao):
            super().add(competicao.id_competicao, competicao)
    
    def remove(self, competicao: Competicao, dados):
        if self.__competicao_valida(competicao):
            super().remove(competicao.participantes(dados))

    def __competicao_valida(self, competicao):
        return (competicao is not None) and (isinstance(competicao, Competicao)) and (isinstance(competicao.id_competicao, int))
