import math
from peca import *

class Logica:
    def __init__(self):

        self.__tabuleiro = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        self.__mov = []
        self.__qtd_linha = 7
        self.__qtd_coluna = 5
        self.__pecas_b = 2
        self.__pecas_p = 2

    def inicia_tabuleiro(self,linha,coluna):
        self.__tabuleiro[linha][coluna] = Peca()

    @property
    def tabuleiro(self):
        return self.__tabuleiro

    @tabuleiro.setter
    def tabuleiro(self,tabuleiro):
        self.__tabuleiro = tabuleiro

    def movimentacao(self,linha_ini,coluna_ini,linha_final,coluna_final):
        if ((self.__tabuleiro[linha_ini][coluna_ini] != 0)and
                (self.__tabuleiro[linha_ini][coluna_ini].nome != "Rainha")):

            if(self.__tabuleiro[linha_final][coluna_final]!=0):
                if(self.__tabuleiro[linha_final][coluna_final].nome == "Rainha"):
                    self.__tabuleiro[linha_final][coluna_final] = \
                        self.__tabuleiro[linha_ini][coluna_ini]
                    self.__tabuleiro[linha_ini][coluna_ini] = 0
                    return self.__tabuleiro[linha_final][coluna_final].cor

                if(self.__tabuleiro[linha_final][coluna_final].cor=='B'):
                    self.__pecas_b-=1
                else:
                    self.__pecas_p-=1

            self.__tabuleiro[linha_final][coluna_final] = \
                self.__tabuleiro[linha_ini][coluna_ini]
            self.__tabuleiro[linha_ini][coluna_ini] = 0

            if(self.__pecas_b==0):
                return self.__tabuleiro[linha_final][coluna_final].cor
            if (self.__pecas_p == 0):
                return self.__tabuleiro[linha_final][coluna_final].cor

