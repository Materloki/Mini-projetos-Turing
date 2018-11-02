##################################################################
##                                                              ##
##      CODIGO CRIADO PELO GRUPO TURING - POLI USP 2017         ##
##      https://www.facebook.com/grupoturing.poliusp            ##
##      Todos podem usar este código livremente                 ##
##                                                              ##
##################################################################

import jogo
import algoritmoGenetico as ag


def main():
    '''

    Nessa funcao voce deve procurar um individuo capaz de vencer o jogo,
    Para isso você precisa:

    1) Declarar a Geracao Zero, com 10 individuos

    2) Jogar o jogo com a geração

    3) Avaliar os individuos de cada geracao (fitness)

    4) Selecionar os 4 melhores e utilizar eles para reproduzir a proxima Geracao

    5) Voltar para "2" até a condição de parada seja atingida (ex: conseguir passar de nível, fazer uma pontuação maior que 20.000 pontos)

    6) Retornar um objeto Geracao com os individuos treinados (pode ser apenas 1 individuo)

    Dicas: você ja criou diversas funcoes no outro arquivo e deve chamá-las quando achar necessário.
      As que você vai precisar usar são:
          -ag.Geracoes()
          -individuo.fitness(gameState)
          -geracao.selecao(numSelec)
          -geracao.reproduzir(m, chanceCO, chanceMut)
       Alem disso, você deve usar a funcão ja pronta:
          -gameState = jogo.jogar(geracao.individuos, numerodageracao, vel_jogo,scoreMax = 20000, jogoRapido = False)
          - geracao.individuos é a geracao criada por você
          - numeroDaGeracao é qual a geração atual (1, 2, 3...)
          - vel_jogo é a velocidade do jogo (1 é a velocidade normal, recomendamos 100 para não ficar esperando muito)
          - scoreMax e jogoRapido estão definidos
          -essa função utiliza o individuo para um novo jogo de Tetris, e retorna variáveis do jogo (gameState)
            além disso, deve-se escolher a pontuação máxima para "ganhar" e finalizar o jogo
            e também definir se o jogo estará rápido (True) ou não (False)

         -lembrando que gameState possui:
                    gameState[0] = numero de pecas
                    gameState[1] = linhas destruidas(combos de 1,2,3,4)
                    gameState[2] = pontuação do tetris
                    gameState[3] = ganhou


    '''
    #COMPLETE AQUI:
    geracao = ag.Geracao(20,7)
    for i in range(20):
      print(geracao.individuos[i])
    epoca = 0
    while geracao.individuos[0].score < 10000 :
        gameState = jogo.jogar(geracao.individuos, epoca, 100,scoreMax = 20000, jogoRapido = False)
        for i in range (len(geracao.individuos)):
            geracao.individuos[i].fitness(gameState[i])
            print(geracao.individuos[i].score)
        geracao.selecao(7)
        geracao.reproduzir(20,0.2, 0.05)
        epoca += 1
    return geracao
    #geracao.selecao(1)
    #print("melhor individuo!!!")
    #gameState = jogo.jogar(geracao.individuos, epoca, 10,scoreMax = 20000, jogoRapido = True)

     



#-----------------------------------------------

gen = main()

## essa parte serve para você ver o melhor individuo jogando o jogo em sua velocidade normal
gen.selecao(1)
print("melhor individuo!!!")
gameState = jogo.jogar(gen.individuos, 1, 1)
print(gen.individuo[0].score)
