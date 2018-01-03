import pygame, sys, os, math
from imagens_jogo import *
from logica_jogo import *
from peca import *

imagem = Imagem()
logica = Logica()

nome_da_peca = ["Cavaleiro","Rainha","Rei"]
cor_da_peca = ["B","P"]
pecas_movidas = []
selecao = []

pygame.init()

display_hidth = 45
display_height = 45
screen = pygame.display.set_mode((display_hidth*5,display_height*7))
pygame.display.set_caption("Chess")
clock = pygame.time.Clock()


crashed = False
# fonte = pygame.font.SysFont("monospace", 20)
# turnindic = fonte.render("Black",True,(139,125,107),(0,0,0,0))
# piecesleft = fonte.render("Peca",True,(139,125,107),(0,0,0,0))
#
# screen.blit(turnindic, (0, display_height*7+10))
# screen.blit(piecesleft, (display_hidth*5-140, display_height*7+10))


def pixelpos(pos): return (pos[0] * display_height, pos[1] * display_hidth)

clock.tick(30)
darktan = (0, 0, 0)
lighttan = (255, 228, 196)


for row in range(7):
    for col in range(5):
        pygame.draw.rect(screen, lighttan, [
            row*90, col*90, display_height, display_hidth])
        pygame.draw.rect(screen, lighttan, [
            row*90+display_height, col*90+display_hidth, display_height, display_hidth])

def inserir_pecas(nome,pref_cor,linha,coluna): #pref == prefixo
    screen.blit(imagem.imagens_da_peca[nome+pref_cor], (coluna * 45, linha * 45))
    logica.inicia_tabuleiro(linha,coluna)
    logica.tabuleiro[linha][coluna].nome = nome
    logica.tabuleiro[linha][coluna].cor = pref_cor

inserir_pecas(nome_da_peca[0],cor_da_peca[0],5,3) # cavaleiro Branco
inserir_pecas(nome_da_peca[0],cor_da_peca[1],1,3) # cavaleiro Preto

inserir_pecas(nome_da_peca[1],cor_da_peca[0],6,2) #Rainha Branca
inserir_pecas(nome_da_peca[1],cor_da_peca[1],0,2) #Rainha Preta

inserir_pecas(nome_da_peca[2],cor_da_peca[0],5,1) #Rei Branco
inserir_pecas(nome_da_peca[2],cor_da_peca[1],1,1) #Rei Preto





def imagem_escolha_tabuleiro(linha,coluna): #definicao da imagem durante a escolha no tabuleiro
    if((logica.tabuleiro[linha][coluna] != 0)):
        if(logica.tabuleiro[linha][coluna].nome != "Rainha"):
            desempilhar_imagens()
            pecas_movidas.append([coluna, linha])
            selecao.append([linha,coluna])
            screen.blit(imagem.escolha, pixelpos((coluna, linha)))
            for i in [-1,1]:
                mov_tabela(linha,coluna,0,i)
                mov_tabela(linha, coluna, i, 0)
    else:
        desempilhar_imagens()


def desempilhar_imagens():
    for i in range(pecas_movidas.__len__()):
        x,y = pecas_movidas.pop()
        if((x <0 or y<0)or(x>6 or y>6)):return
        if ((x + y) % 2 == 0):
            pygame.draw.rect(screen, lighttan, [x*45, y * 45, display_height, display_hidth])
        else:
            pygame.draw.rect(screen, darktan, [x*45, y * 45, display_hidth, display_height])
        if(logica.tabuleiro[y][x] != 0):
            nome = logica.tabuleiro[y][x].nome
            cor =  logica.tabuleiro[y][x].cor
            screen.blit(imagem.imagens_da_peca[nome + cor], (x * 45, y * 45))

def mov_tabela(linha, coluna,x,y):
    if(logica.tabuleiro[y][x] == 0):
        pecas_movidas.append([coluna + x, linha + y])
        screen.blit(imagem.movimento, pixelpos((coluna+x, linha+y)))

#pygame.draw.rect(screen, darktan, [1*45, 0, display_hidth, display_height])

#pygame.draw.rect(screen, lighttan, [0, 1 * 45, display_height, display_hidth])

def troca_imagem(linha,coluna):
    x,y = selecao.pop()
    a = logica.tabuleiro[linha][coluna]
    logica.tabuleiro[linha][coluna] = logica.tabuleiro[x][y]
    logica.tabuleiro[x][y] = a



while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            linhaX = int(math.ceil(mouseY / 45) - 1)
            colunaX = int(math.ceil(mouseX / 45) - 1)
            if(selecao.__len__() ==0):
                imagem_escolha_tabuleiro(linhaX,colunaX)
            else:
                if(pecas_movidas.__contains__([colunaX,linhaX]) and
                       (not selecao.__contains__([linhaX,colunaX]))):
                    troca_imagem(linhaX, colunaX)
                    desempilhar_imagens()
                else:
                    selecao.pop()




    pygame.display.update()
