##################################################################
##                                                              ##
##      CODIGO CRIADO PELO GRUPO TURING - POLI USP 2016         ##
##      https://www.facebook.com/grupoturing.poliusp            ##
##      Todos podem usar este código livremente                 ##
##                                                              ##
##################################################################

import jogo
import AG_pong as ag

def main():
    
##    Nessa funcao voce deve procurar um individuo capaz de vencer o jogo,
##    Para isso você precisa:
##
##    1) Declarar a Geracao Zero, com 10 individuos
##
##    2) Avaliar os individuos de cada geracao (jogando o jogo)
##
##    3) Selecionar os 4 melhores e utilizar eles para reproduzir a proxima Geracao
##
##    4) Voltar para "2" até a condição de parada seja atingida (ex: rebater mais de 30 vezes, fazer uma pontuação maior que X pontos)
##
##    5) Retornar um objeto Geracao com os individuos treinados (pode ser apenas 1 individuo)
##
##
##    Dicas: você ja criou diversas funcoes no outro arquivo e deve chamá-las quando achar necessário.
##        As que você vai precisar usar são:        
##            -ag.Geracoes()
##            -individuo.fitness(gameState)
##            -geracao.selecao(numSelec)
##            -geracao.reproduzir(m, chanceCO, chanceMut)
##        Alem disso, você deve usar a funcão ja pronta:
##            -gameState = jogo.jogar(individuo,numBat,multVelocidade)
##                -essa função utiliza o individuo para jogar uma partida de Pong, e retorna variáveis do jogo (gameState)
##                    além disso, deve-se escolher o número de batidas para "ganhar" e finalizar o jogo
##                    e também definir o quão rápido deve estar o jogo (recomendo usar multVelocidade = 50)
##
##                -lembrando que gameState possui:    
##                    #gameState[0] = player.y (normalizado de -1 a +1)
##                    #gameState[1] = ball.x   (normalizado de -1 a +1)
##                    #gameState[2] = ball.y   (normalizado de -1 a +1)
##                    #gameState[3] = ball.speed_x
##                    #gameState[4] = ball.speed_y
##                    #gameState[5] = numBat (numero de vezes que a bolinha bateu no player)
##                    #gameState[6] = ganhou (True/False, se o player sobreviveu o tempo definido)

    
    #COMPLETE AQUI
    geracao_zero = ag.Geracao(10)

    while geracao_zero.individuos[0].score <= 200:
        for i in range(len(geracao_zero.individuos)):
            gameState = jogo.jogar(geracao_zero.individuos[i], 30, 50)
            geracao_zero.individuos[i].fitness(gameState)
            print(geracao_zero.individuos[i].score)
        geracao_zero.selecao(4)
        geracao_zero.reproduzir(10,0.2, 0.05)

    return geracao_zero
    



#-----------------------------------------------



gen = main()


#essa parte do código serve para exportar os individuos em formato de texto
#nao precisa mexer
for i in range(len(gen.individuos)):
    arq = open('inds.txt', 'w')
    arq.write(' '.join(map(str, gen.individuos[i].pesos)))
    arq.close()

