class Peca:
    def __init__(self):
        self.__cor = ''
        self.__nome = ''
        self.__selecionada= False

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self,cor):
        self.__cor = cor

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    @property
    def selecionada(self):
        return self.__selecionada

    @selecionada.setter
    def selecionada(self,selecionada):
        self.__selecionada = selecionada

    def to_string(self):
        return str(self.__nome+"  "+ self.__cor)
