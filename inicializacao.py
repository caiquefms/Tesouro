import pygame, sys, os, math
from imagens_jogo import *
from logica_jogo import *
from peca import *

nome_da_peca = ["Cavaleiro", "Rainha", "Rei"]
cor_da_peca = ["B", "P"]

class Inicializacao:
    def __init__(self):
        pygame.init()

        self.__imagem = Imagem()
        self.__logica = Logica()

        self.__pecas_selecionadas = []
        self.clicks = []
        self.__round = 'P'

        self.__display_hidth = 45
        self.__display_height = 45
        self.__screen = pygame.display.set_mode(
            (self.__display_hidth * 5, self.__display_height * 7)
        )
        self.__clock = pygame.time.Clock()

        self.__darktan = (0, 0, 0)
        self.__lighttan = (255, 228, 196)

    def imprime_matriz(self):
        for linha in range(7):
            for col in range(5):
                print("[{}][{}] {} ".
                      format(linha, col, self.__logica.tabuleiro[linha][col])
                      , end = ' ')
            print("\n")

    def posicao_pixel(self,coluna,linha):
        return (coluna * self.__display_height, linha * self.__display_hidth)

    def criar_tabuleiro(self):
        for linha in range(7):
            for coluna in range(5):
                pygame.draw.rect(self.__screen, self.__lighttan, [
                    linha * 90, coluna * 90, self.__display_height, self.__display_hidth])
                pygame.draw.rect(self.__screen, self.__lighttan, [
                    linha * 90 + self.__display_height, coluna * 90 + self.__display_hidth,
                    self.__display_height, self.__display_hidth])

    def inserir_pecas(self,nome, pref_cor, linha, coluna):  # pref == prefixo
        self.__screen.blit(self.__imagem.imagens_da_peca[nome + pref_cor],
                           (coluna * 45, linha * 45))
        self.__logica.inicia_tabuleiro(linha, coluna)
        self.__logica.tabuleiro[linha][coluna].nome = nome
        self.__logica.tabuleiro[linha][coluna].cor = pref_cor

    def comando(self,linha,coluna):
        if self.existe_peca(self.__round,linha,coluna):
            if(self.clicks.__len__() == 2):
                self.clicks.pop(0)
            self.desempilhar_imagens()
            self.imagem_escolha_tabuleiro('movimento',linha,coluna)
            self.imagem_escolha_tabuleiro('ataque',linha,coluna)
        else:
            x = self.movimento()
            self.desempilhar_imagens()
            return x

    def existe_peca(self,round,linha,coluna):
        if self.__logica.tabuleiro[linha][coluna] != 0 :
            if((self.__logica.tabuleiro[linha][coluna].nome != "Rainha") and
                   self.__logica.tabuleiro[linha][coluna].cor == round):
                return True
        else:
            return False



    def imagem_escolha_tabuleiro(self,tipo,linha, coluna):
        self.__pecas_selecionadas.append([coluna, linha])

        if(tipo == 'movimento'):
            self.__screen.blit(self.__imagem.escolha,
                               self.posicao_pixel(coluna, linha))
            img = self.__imagem.movimento
            for i in [-1, 1]:
                self.impressao_img(tipo,img,linha, coluna, 0, i)
                self.impressao_img(tipo,img,linha, coluna, i, 0)

        if(tipo == 'ataque'):
            img = self.__imagem.ataque
            for i in [-1, 1]:
                self.impressao_img(tipo,img,linha, coluna, 1, i)
                self.impressao_img(tipo,img,linha, coluna, -1, i)
                self.impressao_img(tipo,img,linha, coluna, i, i)
                self.impressao_img(tipo,img,linha, coluna, i, i)

    def impressao_img(self,tipo,img,linha,coluna,x,y):
        if ((linha + y < 0) or (linha + y > 6)): return
        if ((coluna + x < 0) or (coluna + x > 4)): return

        if(tipo == 'movimento'):
            condicao = self.__logica.tabuleiro[linha +y][coluna + x] == 0
        if(tipo == 'ataque'):
            condicao = ((self.__logica.tabuleiro[linha +y][coluna + x] != 0) and
                        (self.__logica.tabuleiro[linha][coluna].cor !=
                         self.__logica.tabuleiro[linha + y][coluna + x].cor))

        if(condicao):
            self.__pecas_selecionadas.append([coluna + x, linha + y])
            self.__screen.blit(img,self.posicao_pixel(coluna + x, linha + y))


    def desempilhar_imagens(self):
        for i in range(self.__pecas_selecionadas.__len__()):
            x, y = self.__pecas_selecionadas.pop()
            if ((x < 0 or y < 0) or (x > 6 or y > 6)): return
            if ((x + y) % 2 == 0):
                pygame.draw.rect(self.__screen, self.__lighttan,
                                 [x * 45, y * 45,
                                  self.__display_height, self.__display_hidth])
            else:
                pygame.draw.rect(self.__screen, self.__darktan,
                                 [x * 45, y * 45,
                                  self.__display_hidth, self.__display_height])
            if (self.__logica.tabuleiro[y][x] != 0):
                nome = self.__logica.tabuleiro[y][x].nome
                cor = self.__logica.tabuleiro[y][x].cor
                self.__screen.blit(self.__imagem.imagens_da_peca[nome + cor],
                                   (x * 45, y * 45))

    def movimento(self):
        if (self.clicks.__len__() == 2):
            fim = self.clicks.pop()
            inicio = self.clicks.pop()
            if(self.__pecas_selecionadas.__contains__(fim)):
                x = self.__logica.movimentacao(inicio[1],inicio[0],fim[1],fim[0])
                if(self.__round == 'P'):
                    self.__round = 'B'
                else:
                    self.__round = 'P'
                return x
        self.clicks.clear()

    def acabar_jogo(self):
        pygame.draw.rect(self.__screen, self.__darktan,
                         [self.__display_hidth * 45, self.__display_height*45
                         ,self.__display_hidth, self.__display_height])
