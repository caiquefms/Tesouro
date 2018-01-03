import pygame
import os

class Imagem:
    def __init__(self):
        self.__movimento = None
        self.__escolha = None
        self.__ataque = None
        self.__icone = None
        self.__imagens_da_peca = None
        self.__iniciar_imagens()

    def __iniciar_imagens(self):
        self.__imagens_da_peca = {}
        self.__movimento = pygame.image.load(os.path.join("imagens","movimento.png"))
        self.__escolha = pygame.image.load(os.path.join("imagens","escolha.png"))
        self.__ataque = pygame.image.load(os.path.join("imagens","Ataque.png"))
        self.__icone = pygame.image.load(os.path.join("imagens","icon.png"))

        self.__imagens_da_peca["CavaleiroB"] = pygame.image.load(os.path.join("imagens","CavaleiroB.png"))
        self.__imagens_da_peca["CavaleiroP"] = pygame.image.load(os.path.join("imagens","CavaleiroP.png"))

        self.__imagens_da_peca["ReiB"] = pygame.image.load(os.path.join("imagens","ReiB.png"))
        self.__imagens_da_peca["ReiP"] = pygame.image.load(os.path.join("imagens","ReiP.png"))

        self.__imagens_da_peca["RainhaB"] = pygame.image.load(os.path.join("imagens","RainhaB.png"))
        self.__imagens_da_peca["RainhaP"] = pygame.image.load(os.path.join("imagens","RainhaP.png"))

    @property
    def imagens_da_peca(self):
        return self.__imagens_da_peca

    @property
    def icone(self):
        return self.__icone

    @property
    def ataque(self):
        return self.__ataque

    @property
    def movimento(self):
        return self.__movimento

    @property
    def escolha(self):
        return self.__escolha
