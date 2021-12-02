#Bibliotecas
import pygame
import sys
import time

#Inicialização pygame
pygame.init()

#Criação de objeto 'tela' com alt e comp 600px
size = width, height = 600, 600
screen = pygame.display.set_mode(size)

black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
cores = [black, white, red, green, blue]
#x = 0

#Carrega as imagens:
xis = pygame.image.load("xis.png")
bola = pygame.image.load("bola.png")

xis = pygame.transform.scale(xis, (100, 100))
bola = pygame.transform.scale(bola, (100, 100))

#jogares = [xis, bola]
jogadores_paralelos = [' ', ' ']
#Preenche a tela com a cor 'white':
screen.fill(cores[1])

#Definição dos quadrantes:
quadrante_linha = [50, 250, 450]
quadrante_coluna = [50, 250, 450]

matriz_paralela = [[' ',' ',' '],
                   [' ',' ',' '],
                   [' ',' ',' ']]

def desenha_quadro():
    pygame.draw.line(screen, black, (200, 0), (200, 600), 5)
    pygame.draw.line(screen, black, (400, 0), (400, 600), 5)

    pygame.draw.line(screen, black, (0, 200), (600, 200), 5)
    pygame.draw.line(screen, black, (0, 400), (600, 400), 5)

#def xis_posicao():
    #screen.blit(xis, (50, 50))
    #screen.blit(xis, (50, 250))
    #screen.blit(xis, (50, 450))
    #screen.blit(xis, (250, 50))
    #screen.blit(xis, (250, 250))
    #screen.blit(xis, (250, 450))
    #screen.blit(xis, (450, 50))
    #screen.blit(xis, (450, 250))
    #screen.blit(xis, (450, 450))

#def bola_posicao():
    #screen.blit(bola, (50, 50))
    #screen.blit(bola, (50, 250))
    #screen.blit(bola, (50, 450))
    #screen.blit(bola, (250, 50))
    #screen.blit(bola, (250, 250))
    #screen.blit(bola, (250, 450))
    #screen.blit(bola, (450, 50))
    #screen.blit(bola, (450, 250))
    #screen.blit(bola, (450, 450))

#listax: [0,0,0,0,0]    Tentativa de criar listas para adição de valores (matriz 'espelho') após def faz_jogada.
#listaxb:[0,0,0,0,0]

def faz_jogada(pos):
    index_linha = int(pos[0]/200)
    index_coluna = int(pos[1]/200)
    if(matriz_paralela[index_coluna][index_linha]) == (' '):
        matriz_paralela[index_coluna][index_linha] = 'X'
        print(matriz_paralela)
        screen.blit(xis,(quadrante_linha[index_linha], quadrante_coluna[index_coluna]))
    else:
        print("Posição Ocupada")

        
    
    
def faz_jogadao(poso):
    index_linha = int(poso[0]/200)
    index_coluna = int(poso[1]/200)
    if(matriz_paralela[index_coluna][index_linha]) == (' '):
        matriz_paralela[index_coluna][index_linha] = 'O'
        print(matriz_paralela)
        screen.blit(bola,(quadrante_linha[index_linha], quadrante_coluna[index_coluna]))
    else:
        print("Posição Ocupada")

def vencedorx():
    if matriz_paralela[0][0] == matriz_paralela[0][1] == matriz_paralela[0][2]:
        print("XABLAU X!")
    if matriz_paralela[1][0] == matriz_paralela[1][1] == matriz_paralela[1][2]:
        print("XABLAU X!")
    if matriz_paralela[2][0] == matriz_paralela[2][1] == matriz_paralela[2][2]:
        print("XABLAU X!")
    if matriz_paralela[0][0] == matriz_paralela[1][0] == matriz_paralela[2][0]:
        print("XABLAU X!")
    if matriz_paralela[0][1] == matriz_paralela[1][1] == matriz_paralela[2][1]:
        print("XABLAU X!")
    if matriz_paralela[0][2] == matriz_paralela[1][2] == matriz_paralela[2][2]:
        print("XABLAU X!")
    if matriz_paralela[0][0] == matriz_paralela[1][1] == matriz_paralela[2][2]:
        print("XABLAU X!")
        

def vencedoro():
    if matriz_paralela[0][0] == matriz_paralela[0][1] == matriz_paralela[0][2]:
        print("XABLAU O!")
    if matriz_paralela[1][0] == matriz_paralela[1][1] == matriz_paralela[1][2]:
        print("XABLAU O!")
    if matriz_paralela[2][0] == matriz_paralela[2][1] == matriz_paralela[2][2]:
        print("XABLAU O!")
    if matriz_paralela[0][0] == matriz_paralela[1][0] == matriz_paralela[2][0]:
        print("XABLAU O!")
    if matriz_paralela[0][1] == matriz_paralela[1][1] == matriz_paralela[2][1]:
        print("XABLAU O!")
    if matriz_paralela[0][2] == matriz_paralela[1][2] == matriz_paralela[2][2]:
        print("XABLAU O!")
    if matriz_paralela[0][0] == matriz_paralela[1][1] == matriz_paralela[2][2]:
        print("XABLAU O!")
                  
                    
    
vez = "x"
rodada = 0
#z = 0
while True:
#for z in range(0, 10):
    desenha_quadro()
    
    if rodada >= 9:
        break
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
        if(vez == "x"):
            #print("Vez de X")
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_pos = pygame.mouse.get_pos()
                faz_jogada(click_pos)
                
                rodada = rodada + 1
                vencedorx()
                vez = "o"

        
               

        elif(vez == "o"):
            #print("Vez de O")
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_pos = pygame.mouse.get_pos()
                faz_jogadao(click_pos)
                
                rodada = rodada + 1
                vencedoro()
                vez = "x"

    pygame.display.flip()
                                                        # A partir daqui, ficou a dificuldade em realizar a validação do vencedor e principalmente fazer o loop parar. 
                                                        # Pensei em realizar a validação por igualdade de setores. A validação foi identificada por XABLAU11 ou XABLAU22
                                                        # ...como maneira de identificar qual está sendo obtido. O problema verificado é O LOOP NÃO PÁRA.

                                                        # Como melhora no código ficou pendente uma maneira do loop parar assim que o vencedor for conhecido.
                                                        # Melhora 2: Ao invés de ter duas funções, uma pra cada player, criar uma lista de players e utilizar apenas uma função...
                                                        # ...variando apenas o player na lista.
                                                        # Melhora 3: Assim que o vencedor for conhecido, aplicar uma linha onde o conjunto foi aplicado ('ooo' / 'xxx')
                                                        # Melhora 4: O jogo aplica o vencedor TODAS AS VEZES não importando qual o player...

                                                        
                                                        
    
    #xis_posicao()
    #bola_posicao()
    
    
    

    #screen.fill(black)
    #time.sleep(5)
    #pygame.display.flip()

    #if x == '10':
    #    print(x)
    #    screen.fill(white)

    #elif x == '20':
    #    screen.fill(black)
    #    x = 0
    #screen.fill(white)
    #screen.blit(ball,ballrect)
    #pygame.display.flip()
