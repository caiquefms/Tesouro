from inicializacao import *

sair = False
round = 0
inicializacao = Inicializacao()
inicializacao = Inicializacao()
inicializacao.criar_tabuleiro()

inicializacao.inserir_pecas(nome_da_peca[0],cor_da_peca[0],5,3) # cavaleiro Branco
inicializacao.inserir_pecas(nome_da_peca[0],cor_da_peca[1],1,3) # cavaleiro Preto

inicializacao.inserir_pecas(nome_da_peca[1],cor_da_peca[0],6,2) #Rainha Branca
inicializacao.inserir_pecas(nome_da_peca[1],cor_da_peca[1],0,2) #Rainha Preta

inicializacao.inserir_pecas(nome_da_peca[2],cor_da_peca[0],5,1) #Rei Branco
inicializacao.inserir_pecas(nome_da_peca[2],cor_da_peca[1],1,1) #Rei Preto

while not sair:

    for event in pygame.event.get():  # Recebe os eventos

        if event.type == pygame.QUIT:
            sair = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            linha = int(math.ceil(mouseY / 45) - 1)
            coluna = int(math.ceil(mouseX / 45) - 1)
            if(not inicializacao.clicks.__contains__([coluna,linha])):
                inicializacao.clicks.append([coluna,linha])
            x = inicializacao.comando(linha,coluna)
            if(x!= None):
                sair = True



    pygame.display.update()
