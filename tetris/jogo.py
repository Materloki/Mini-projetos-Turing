import random, pygame

import tetris as t
import algoritmoGenetico as ag

#size = [640, 480]
#screen = pygame.display.set_mode((size[0], size[1]))

#add individuo,
def jogar(individuos, numeroDaGeracao, multVel, scoreMax = 20000, jogoRapido = True):

    numInd = len(individuos)

    t.FPS = int(multVel)
    t.main(telaX = 120 * ((numInd-1)%5) + 220, telaY = 260 * ((numInd-1)//5 + 1), boxSize = 10)

    board = [t.getBlankBoard() for i in range(len(individuos))]

    score = [0 for i in range(numInd)]

    #   ??? deveria estar dentro de individuo ???
    pecasJogadas = [0 for i in range(numInd)]
    linhasDestruidas = [[0,0,0,0] for i in range(numInd)] #combos

    vivo = [True for i in range(numInd)]
    ganhou = [False for i in range(numInd)]

    nextPiece = t.getNewPiece()

    while vivo !=  [False] * numInd : #game loop
        '''
        #process
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print ("Game exited by user")
                exit()
        '''

        fallingPiece = nextPiece
        nextPiece = t.getNewPiece()

        #decide a melhor jogada baseado no que acha (pesos)
        for i in range(len(individuos)):
            if vivo[i]:
                individuos[i].calcularMelhorJogada(board[i], fallingPiece, True)

                if not t.isValidPosition(board[i], fallingPiece):
                    #nao existe possiçao que caiba na tela
                    vivo[i] = False
                else:
                    pecasJogadas[i] +=1
                    score[i] += 1

                    t.addToBoard(board[i], fallingPiece)
                    numLines = t.removeCompleteLines(board[i])
                    if(numLines == 1):
                        score[i] += 40
                        linhasDestruidas[i][0] += 1
                    elif (numLines == 2):
                        score[i] += 120
                        linhasDestruidas[i][1] += 1
                    elif (numLines == 3):
                        score[i] += 300
                        linhasDestruidas[i][2] += 1
                    elif (numLines == 4):
                        score[i] += 1200
                        linhasDestruidas[i][3] += 1

                    #condiçao de parada
                    if score[i] > scoreMax:
                        vivo[i] = False
                        ganhou[i] = True

        #if not jogoRapido:
        desenharNaTela(board,score, 1, nextPiece, fallingPiece, numeroDaGeracao)

    # retorna [numero de pecas, linhas destruidas(combos de 1,2,3,4), score normal de tetris, ganhou]
    gameState = [[pecasJogadas[i], linhasDestruidas[i] ,score[i], ganhou[i]] for i in range(numInd)]
    return(gameState)




def desenharNaTela(board,score,level,nextPiece,fallingPiece, numeroDaGeracao):
    t.DISPLAYSURF.fill(t.BGCOLOR)
    jogosLinha = 5
    for i in range(len(score)):
        t.drawBoard(board[i], margemX = 10+ 120 * (i % jogosLinha), margemY =(i//jogosLinha) * 260 + t.TOPMARGIN) #list

        t.drawStatus(score[i], level, margemX = 20+120* (i % jogosLinha), margemY =(i//jogosLinha) * 260) #list int

        t.drawGeneration(numeroDaGeracao)
        #t.drawNextPiece(nextPiece)
    #if fallingPiece != None:
        #t.drawPiece(fallingPiece, -100)

    pygame.display.update()

    t.FPSCLOCK.tick(t.FPS)




#if __name__ == '__main__':
#    numPesos = 7
#    pesos0 = numPesos*[0]
#    for k2 in range (0,numPesos):
#       pesos0[k2] = 2*random.random()-1
#    pesos0= [-0.97, 5.47, -13.74, -0.73,  7.99, -0.86, -0.72]
#    pesos1 = numPesos*[0]
#    for k2 in range (0,numPesos):
#        pesos1[k2] = 2*random.random()-1
#    pesos1= [1,1,1,1,1,1,1]
#
#
#    indiv = ag.Individuo(pesos0)
#    indiv2 = ag.Individuo(pesos1)

#    print(jogar([indiv,indiv2],300,scoreMax = 200000))
