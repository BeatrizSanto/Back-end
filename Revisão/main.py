
nome = 'bia'
idade = 25
cfp = 567.234
aluno = True
dia = None
print(dia)


#condições

login = input('Digite a senha:')

if login == '1234' or login == '0000':
    print('Parabéns!!!!!!!!')
else:
    print('Senha  incorreta!')

    ##list,dict e tuple
    frutas = ['uva','laranja','Banana']
    print(type(frutas))

    filmes = ("x-men",'carros')
    print(type(filmes))
    print(len(filmes))
    numeros =(10,50,66,90,2,30)
    print(max(numeros))
    print(min(numeros))
    print(sum(numeros))

    #Loops

    resposta = input('Deseja continuar? [s/n]')

    while  resposta == 's':
        print('Executei!')