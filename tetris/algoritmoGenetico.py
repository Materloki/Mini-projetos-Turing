########################################################################################
##                                                                                    ##
##      CODIGO CRIADO PELO GRUPO TURING - POLI USP 2017                               ##
##      https://www.facebook.com/grupoturing.poliusp                                  ##
##      Todos podem usar este codigo livremente                                       ##
##                                                                                    ##
########################################################################################


import random        # importa biblioteca da função aleatória (random)
import tetris as t   # importa o arquivo tetris que será chamado de t


class Individuo():
    '''
    O vetor de pesos dará as diretrizes de como o seu indivíduo vai jogar e calcular a melhor jogada possível. Com esse vetor e
    um vetor de entrada, seu indivíduo vai calcular a melhor direção (direita, esquerda e rotação) para a sua peça ser encaixada!

    Reflexão: O que o vetor entrada contem?
    '''

    #---------------------------------------------------------------------------

    def __init__(self,pesos):
        '''
            OBJETIVO: Inicializar o individuo

            Este é o construtor de um indivíduo, ou seja, para gerar uma
            nova instância de indivíduo, o programa chama esta função.
            Lembre-se que cada indivíduo será, na verdade, um jogo(uma partida) de Tetris!

            Ao criar um indivíduo, a notação em Python a ser seguida é:

                NomeDoObjeto = NomeDaClasse(atributo1, atributo2, etc.)

            O atributo (pesos) é o único a ser fornecido neste caso.
            Cada peso funciona como o gene do indivíduo.

            Não é necessário escrever (self) ao criar um novo indivíduo.

            Exemplo: novo_individuo = Individuo([1.2123, 3.4123, -5.4123, ...])
                                                    ^
                                                    ^
                                                 lista de pesos

            Você inicializará o indivíduo com um score nulo e um vetor de pesos

            APAGUE O TRECHO "pass" ao final desta função
            ESCREVA código necessário para implementá-la.

            Lembre-se de apagar o trecho "pass" nas funções seguintes
            '''
            # COMPLETE AQUI:

            # self.pesos = ??
            # self.score = ??
        self.pesos = pesos
        self.score = 0

            

    #---------------------------------------------------------------------------

    def __str__(self):
        s = "   Pesos:"
        for i in range(len(self.pesos)):
            s+= "%5.2f "%(self.pesos[i])
        return s
        '''
            Essa função não precisa ser implementada!

            retorna o print do indivíduo, apresentando os pesos do mesmo
            de maneira mais fácil de ler.

            Ex: Suponha que tenhamos um indivíduo (ind1) com a
            seguinte lista de pesos:

            [1.214154,  3.414821, -5.4184512]

            Se executarmos o comando 'print(ind1)', teremos:

            >>>print(ind1)
            Pesos: 1.21  3.41 -5.41

            '''


    #---------------------------------------------------------------------------

    def fitness(self,gameState):
        '''
            Esta função determinará a pontuação de cada indivíduo ao final
            de uma rodada, atualizando o atributo score deste indivíduo.

            OBJETIVO: Implementar a função fitness, que avalia o desempenho
                      de um indivíduo e atualiza o atributo (self.score).

            Essa função recebe como entrada a variável gameState,
            que é uma lista com informações do jogo. A partir dela,
            é possível saber qual era o estado do jogo quando ele acabou.

                Informações em cada posição da lista:

                    gameState[0] = inteiro com o numero de pecas
                    gameState[1] = vetor com as linhas destruidas combos de 1,2,3,4 linhas destruidas
                    gameState[2] = inteiro com a pontuação do tetris
                    gameState[3] = booleano


            Perceba que gameState será fornecida a partir do programa do jogo,
            que é um código pronto, no qual vocês não devem fazer modificações.

            Sejam criativos, e imaginem quais dos parâmetros acima
            vocês deveriam usar para avaliar o desempenho de um jogo

            '''
            # COMPLETE AQUI:

            # self.score = ??
        self.score = 0
        self.score += gameState[0]
        self.score = self.score + gameState[2]
        if gameState[3]:
            self.score += 100
        for i in range(len(gameState[1])):
            self.score += gameState[1][i]                


    #---------------------------------------------------------------------------

    def calcularMelhorJogada(self, board, peca, jogoRapido = False):
          '''
          Essa funcao nao precisa ser implementada!

          OBJETIVO: Escolher qual a melhor jogada para o individuo executar naquele momento

          Aqui o seu indivíduo vai selecionar a direção (direita, esquerda e rotação) em que a nova peça será colocada no jogo!
          Como ele vai fazer isso? Simples! Ele verá todas as possiveis jogadas (todas as rotações e posições possiveis) e
          ira calcular um score para cada uma delas.

          A jogada escolhida será aquela com o maior score

          Esse score será calculado na função calcularPontuacaoDaJogada() implementada a seguir

          '''
          melhorX = 0 #posicao em x
          melhorR = 0 #rotacao da peca
          melhorY = 0
          melhorScore = -100000 #menor do q qualquer valor de score

          #calcula buracos e tampas inicias
          buracosTotaisAntes, tampasTotaisAntes = t.calcularInfosIniciais(board)

          for r in range(len(t.PIECES[peca['shape']])):  #itera em todas as rotaçoes possiveis
              for x in range(-2,t.BOARDWIDTH-2):         #iterar todas as posicoes possiveis

                  #retorna: [jogadaValida, alturaTotal, numLinhasCompletas, buracosFormados, tampasFormadas, ladosPecas, ladosChao, ladosParede]
                  infoJogada = t.calcularInfosDaJogada(board, peca, x, r, buracosTotaisAntes, tampasTotaisAntes)
                  if infoJogada[0]: #jogadaValida

                      #self.pesos = [-3.78, 1.6, -2.31, -0.59, 4.0, 0.65, 6.52]

                      #calcular score do movimento
                      scoreMovimento = self.calcularPontuacaoDaJogada(infoJogada)
                      #atualiza o melhor movimento
                      if scoreMovimento > melhorScore:
                          melhorScore = scoreMovimento
                          melhorX = x
                          melhorR = r
                          melhorY = peca['y'] #p ir mais rapido

          if jogoRapido:
              peca['y'] = melhorY
          else:
              peca['y'] = -2
          peca['x'] = melhorX
          peca['rotation'] = melhorR
          #print(melhorX,"   ", melhorR)
          return melhorX, melhorR



    def calcularPontuacaoDaJogada(self, infoJogada):
        '''
        OBJETIVO: Calcular pontuação da possível jogada atual

        Esse score será calculado a partir das informações que ele recebe do jogo no vetor infoJogada:

        infoJogada[0] = jogadaValida
        infoJogada[1] = alturaTotal
        infoJogada[2] = numLinhasCompletas
        infoJogada[3] = buracosFormados
        infoJogada[4] = tampasFormadas
        infoJogada[5] = ladosPecas
        infoJogada[6] = ladosChao
        infoJogada[7] = ladosParede

        Dica: Toda jogada testada aqui já é válida

        Esse vetor de entrada e os pesos serão utilizados para obter o score

        '''
        # COMPLETE AQUI:
        scoreMovimento = 0
        for i in range(len(self.pesos)):
            scoreMovimento += self.pesos[i]*infoJogada[i+1]
        
        return scoreMovimento




#########################################################################################

class Geracao:
    '''
    A Geracao é onde ocorre toda a evolução,

        Esta classe possui o atributo:
               -individuos: uma lista de objetos da classe Individuo

        E possui as funções:
               -selecao
               -reproduzir
               -CrossOver
               -Mutacao
    '''

    #---------------------------------------------------------------------------

    def __init__ (self, numInd, numPesos):
        
       '''
            Este é o construtor de uma geração.

            O objeto Geracao deve ter um atributo (individuos), que é
            uma lista de indivíduos.

            Para isso, crie uma lista de indivíduos com (numInd) indivíduos,
            cada um com uma distribuição randômica de pesos
            que contenha 7 pesos.

            '''

            # COMPLETE AQUI:

            # self.individuos = individuos
       self.individuos = []
       for i in range(numInd):
          pesos = []
          for j in range(numPesos):
             pesos.append(random.uniform(-10, 10))
          self.individuos.append(Individuo(pesos))


    #---------------------------------------------------------------------------

    def __str__(self):

        '''
        Não precisa implementar!

        Retorna o print da geração fácil de ler

        '''
        for i in range(len(self.individuos)):
            print("Individuo %d:"%i)
            print(self.individuos[i])
        return ''

    #---------------------------------------------------------------------------

    def selecao(self, numSelec):

        '''
            OBJETIVO: selecionar os melhores indivíduos e eliminar os demais
                    da lista comparando os scores. Manipule a lista de modo
                    que apenas os melhores permaneçam na geração.
                    Para isso, encontre os melhores individuos percorrendo a lista

                    A lista atualizada deverá ter tamanho (numSelec).

                    Dicas: O python permite mudar o tamanho das listas,
                           logo não é necessário criar uma nova lista.

                           Exemplo: lista = [0, 3 , 4, 5]
                           >>> lista.pop()
                           >>> print(lista)
                           >>> [0, 3, 4]
                           >>> lista.append(2)
                           >>> print(lista)
                           >>> [0, 3, 4, 2]

                           Essa função não precisa retornar nada,
                           apenas alterar variáveis já existentes
            '''

            # COMPLETE AQUI
        for j in range(1, len(self.individuos)):
            valor = self.individuos[j]
            i = j - 1
            while i > -1 and self.individuos[i].score < valor.score :
              self.individuos[i+1] = self.individuos[i]
              i -= 1
            self.individuos[i + 1] = valor


        indice = len(self.individuos) - 1
        while indice >= numSelec:
          self.individuos.pop(indice)
          indice -= 1


    #--------------------------------------------------------------------------

    def CrossOver(self, individuo1, individuo2, chanceCO):
            '''
            O Crossing-Over consiste em trocar trechos de indivíduos.
            No nosso exemplo, deveremos sortear aleatoriamente uma posicao
            da lista de pesos e permutar os pesos dessa posicao entre dois
            indivíduos. Esta permutacao deverá ocorre com chanceCO.

            OBJETIVO: Aplicar o crossing over com (chanceCO) de acontecer.

                Para isso, voce deve receber 2 objetos do tipo individuo.
                Lembrem-se que os valores trocados devem ter o mesmo locus!
                "Gene de cabelo nao troca com gene de olho"
                Dicas: A função random.random() retorna um float
                       aleatório entre 0 e 1.

                       A função CrossOver não precisa retornar nada,
                       apenas alterar individuo1 e individuo2 já existentes.
            '''

            # COMPLETE AQUI:
            locus = 0
            AUX = 0
            if random.random() <= chanceCO:
                          locus = random.randint(0,6)
                          AUX = individuo1.pesos[locus]
                          individuo1.pesos[locus] = individuo2.pesos[locus]
                          individuo2.pesos[locus] = AUX

    #---------------------------------------------------------------------------

    def Mutacao(self, individuo1, chanceMut):
        '''
            OBJETIVO: Aplicar uma mutação com (chanceMut) de chance em cada peso do (individuo)
                    Existem diversas maneiras de fazer isso
                    Sugerimos fortemente que a mutação seja multiplicar o peso por um valor randômico entre -1.1 e 1.1
                    dica: a funcao random.random() retorna um float entre 0 e 1
                    dica: essa funcao nao precisa retornar nada, apenas alterar individuo já existente

                    Reflexão: quantos valores diferentes esse numero randomico pode assumir dentro do intervalo de [-1,1]?
            '''

                #COMPLETE AQUI:
        if random.random() <= chanceMut:
           locus = random.randint(0,6)
           individuo1.pesos[locus] = random.uniform(-1.1, 1.1)*individuo1.pesos[locus]
            



    #---------------------------------------------------------------------------

    def reproduzir(self, m, chanceCO = 0.2, chanceMut = 0.15):
        '''
                OBJETIVO:
                        Aumentar o numero de individuos  de n (=len(self.individuos)) que corresponde a geração atual selecionada
                        para (m) individuos (não é necessário retestar quem possui o melhor score)
                        Aplica-se o crossing over e a mutacao nos novos individuos
                        Existem diversas maneiras de fazer isso

                        dica: voce deve chamar as funcoes CrossOver e Mutacao (faca elas primeiro)
                        dica: Cuidado! Se voce fizer individuoA = individuoB,
                                O python passara por referencia e toda mudanca que voce fizer em individuoA, ocorrera no individuoB (e vice-versa).
                                O mesmo vale para listas
                                O jeito correto de fazer isso e: individuoA = individuoB(individuoA.pesos[:])
                                (Nao necessariamente voce vai precisar usar isso, foi so um aviso previo que faz muita gente erra por motivos de python)
                        dica: essa funcao nao precisa retornar nada, a geracao e alterada globalmente
                '''

                #COMPLETE AQUI:
        restam = m - len(self.individuos)
        novo_individuo = []
        i = 0
        while restam > 0:
                novo_individuo = Individuo(self.individuos[i].pesos[:])
                self.CrossOver(novo_individuo,self.individuos[i+1], chanceCO)
                self.Mutacao(novo_individuo, chanceMut)
                self.individuos.append(novo_individuo)
                i += 1
                restam -= 1
                if i == (m-1):
                        i = 0
    #---------------------------------------------------------------------------
