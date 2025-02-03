from math import comb

class probabilidade:
    ''' 
    Calcule a probabilidade de certos jogos de loteria.
    
    Esta classe calcula a probabilidade de acerto de uma cartela em jogos de loteria brasileira.
    '''

    def _init_(self) -> None:

'''
Inicializa a instância da classe 'probabilidade'.

Esta classe calcula a probabilidade de acerto de uma  uma cartela em jogos de loteria brasileira.

jogos disponíveis: 
>>> megasena()
>>> lotofacil()
>>> quina()
'''
self . _jogos_disponiveis  = {
                'Mega-Sena' : {
                    'aposta mínima' : 6 ,
                    'aposta máxima' : 20 ,
                    'números totais' : 60 ,
                },
                'Lotofácil' : {
                    'aposta mínima' : 15 ,
                    'aposta máxima' :  20 ,
                    'números totais' :  25 ,
                },
                'Quina' : {
                    'aposta mínima' : 5 ,
                    'aposta máxima' :  15 ,
                    'números totais' : 80,
                },
}

def  megasena ( self , cartela = [],
                       quantidade_acertos = 6 ,
                       return_string = Verdadeiro ,
                       ) ->  int :
                        '''
        Calcule a probabilidade de acerto em um jogo da Mega-Sena.
        Nesse jogo é necessário de 6 a 20 números em uma cartela.
        Ao chamar a função sem declarar o parâmetro cartela,
        será calculado a probabilidade de acerto em um jogo tradicional.
        Parâmetros:
            cartela (lista): Lista contendo números apostados.
            quantidade_acertos (int): Quantidade de números a acertar.
            return_string (bool): retorna como uma string formatada
                                  com separadores de milhares.
        Retorna:
            apostas_necessarias (int): Quantidade teórica de apostas
                                       necessários para um certo.
        '''
        jogo  =  'Mega-Sena'
        apostas_necessarias  =  self . _calc ( jogo , cartela , quantidade_acertos )
        se  return_string :
            apostas_necessarias  =  self . _formato ( apostas_necessarias )
        retornar  apostas_necessarias

    def  lotofacil ( self , cartela = [],
                        quantidade_acertos = 15 ,
                        return_string = Verdadeiro ,
                        ) ->  int :
                         '''
        Calcule a probabilidade de acerto em um jogo da Lotofácil.
        Nesse jogo é necessário de 15 a 20 números em uma cartela.
        Ao chamar a função sem declarar o parâmetro cartela, será
        calculando a probabilidade de acerto em um jogo tradicional.
        Parâmetros:
            cartela (lista): Lista contendo números apostados.
            quantidade_acertos (int): Quantidade de números a acertar.
            return_string (bool): retorna como uma string formatada
                                  com separadores de milhares.
        Retorna:
            apostas_necessarias (int): Quantidade teórica de apostas
                                       necessários para um certo.
        '''
        jogo  =  'Lotofácil'
        apostas_necessarias  =  self . _calc ( jogo , cartela , quantidade_acertos )
        se  return_string :
            apostas_necessarias  =  self . _formato ( apostas_necessarias )
        retornar  apostas_necessarias

    def  quina ( self , cartela = [],
                    quantidade_acertos = 5 ,
                    return_string = Verdadeiro ,
                    ) ->  int :
        '''
        Calcule a probabilidade de acerto em um jogo da Quina.
        Nesse jogo é necessário de 5 a 15 números em uma cartela.
        Ao chamar a função sem declarar o parâmetro cartela, será
        calculando a probabilidade de acerto em um jogo tradicional.
        Parâmetros:
            cartela (lista): Lista contendo números apostados.
            quantidade_acertos (int): Quantidade de números a acertar.
            return_string (bool): retorna como uma string formatada
                                  com separadores de milhares.
        Retorna:
            apostas_necessarias (int): Quantidade teórica de apostas
                                       necessários para um certo.
        '''
        jogo  =  'Quina'
        apostas_necessarias  =  self . _calc ( jogo , cartela , quantidade_acertos )
        se  return_string :
            apostas_necessarias  =  self . _formato ( apostas_necessarias )
        retornar  apostas_necessarias
    
    def  _calc ( self , jogo : str ,
                    carta = [],
                    quantidade_acertos = 1 ,
                    ) ->  int :
        '''
        Calcule a probabilidade de acerto em um jogo específico.
        Parâmetros:
            jogo (str): Nome do jogo específico a calcular.
            cartela (lista): Lista contendo números apostados.
            quantidade_acertos (int): Quantidade de números a acertar.
        Retorna:
            apostas_necessarias (int): Quantidade teórica de apostas
                                       necessários para um certo.
        '''
        parâmetros  =  self . _jogos_disponiveis [ jogo ]
        aposta_minima  =  parâmetros [ 'aposta mínima' ]
        aposta_máxima  =  parâmetros [ 'aposta máxima' ]
        numero_base  =  aposta_minima
        numeros_totais  =  parâmetros [ 'números totais' ]
        quantidade_apostas  =  1
        se  não for  carta :
            quantidade_numeros  =  numero_base
        elif  isinstance ( cartela , int ):
            quantidade_numeros  =  cartela
        elif  isinstance ( cartela [ 0 ], lista ):
            quantidade_apostas  =  len ( cartela )
            quantidade_numeros  =  len ( cartela [ 0 ])
        elif  isinstance ( carta , lista ):
            quantidade_numeros  =  len ( cartela )
        outro :
            raise  ValueError ( 'O parâmetro "cartela" deve ser do tipo lista '
                             f'ou número inteiro, { type ( cartela ) } foi usado.' )
        se  não  aposta_minima  <=  quantidade_numeros  <=  aposta_maxima :
            raise  ValueError ( f'Cartela da { jogo } deve ter entre '
                             f' { aposta_mínimo } e { aposta_máxima } números.' )
        se  não  0  <  quantidade_acertos  <=  quantidade_numeros :
            raise  ValueError ( f'O parâmetro "quantidade_acertos" deve ser '
                             f'entre 1 e { quantidade_numeros } .' )
        probabilidade  =    pente ( numero_base , quantidade_acertos ) \
                        *  pente ( numeros_totais - numero_base , quantidade_numeros - quantidade_acertos ) \
                        /  comb ( números_totais , quantidade_numeros )
        apostas_necessarias  =  rodada ( 1  /  probabilidade  /  quantidade_apostas )
        # P = C(6, 6) / C(60, 6) = 1 / 50.063.860
        retornar  apostas_necessarias

    def  _format ( self , numero : int ) ->  str :
        '''
        Formatar um número inteiro como uma string formatada com
        separadores de milhares.
        Como por exemplo:
        >>> _formato(5000000)
        '5.000.000'
        Parâmetros:
            numero (int): Número inteiro a formatar.
        Retorna:
            numero (str): Número formatado com separadores de milhares.
        '''
        numero  =  formato ( int ( numero ), ',' ) # resultado em '5.000.000'
        numero  =  numero . substitua ( ',' , '.' ) # resultado em '5.000.000'
        retornar  numero


se  __nome__  ==  '__principal__' :

    prob  =  Probabilidade ()

    # imprimir documentação para auxiliar ao usuário que não deve ser inserida
    documentação  =  prob . megasena . __doc__
    imprimir ( documentação )

    quantidade_numeros  =  entrada ( ' \n '
                               'Digite a quantidade de números para'
                               'uma carta para calcular a probabilidade'
                               'de certo: '
                               ' \n ' )
    enquanto  quantidade_numeros :
        imprimir ( ' \n '
              'Probabilidade de acerto teórico para uma cartela com'
              f' { quantidade_numeros } números: ' )
        quantidade_numeros  =  int ( quantidade_numeros )
        # para n em [quadra, quina, sena]
        para  n  no  intervalo ( 4 , 6 + 1 ):
            apostas_necessarias  =  prob . megasena ( quantidade_numeros ,
                                                quantidade_acertos = n )
            print ( f'• { apostas_necessarias } apostas são permissão '
                  f'para um acerto de { n } números;' )
        quantidade_numeros  =  entrada ( ' \n '
                                   'Digite a quantidade de números para'
                                   'uma carta para calcular a probabilidade'
                                   'de certo: '
                                   ' \n ' )
         