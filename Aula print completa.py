
valor1 = int(152.5266)     
valor2 = int(526.2)
valor3 = int(187.355) 

#print("Valor1 =", valor1, "\nValor2 =", valor2, "\nValor3 =", valor3)

    #print exibe uma mensagem na tela do pc (ou no terminal).

    #\n joga o texto para a linha abaixo.

#print("Valor1 = {:010.2f} \nValor2 = {:010.2f} \nValor3 = {:10.2f}".format(valor1, valor2, valor3))

    #no comando format(), ele posiciona um valor sempre que encontrar {} no texto.

    #{:.2f} indica que deve apenas mostrar duas casas decimais

    #{:10 } indica quantas casas o valor deve ocupar
    #{:010 } indica que deve ocupar 10 casas e prencher as sem valor com 0

    #{:010.5f} indica que o valor deve ocupar 10 casas, preencher as sem valor com 0 e mostrar apenas 5 casas decimais após o . (sempre usar o f)


#print("Valor1 = {v2:10.3f} \nValor2 = {v3:10.3f} \nValor3 = {v1:10.3f}".format( v1=valor1, v2=valor2, v3=valor3))

    #podemos adicionar pseudonimo aos valores para organizarmos da melhor forma (ex:v1,v2 e v3)

#print(f"Valor1 = {valor1:10.3f}; \nValor2 = {valor2:10.3f}; \nValor3 = {valor3:10.3f}. ")

    #no print(f) colocamos diretamente entre {} o valor que gostariamos de exibir
    
    #usamos int() para transformarmos o número em inteiro. ex: valor1 = int(152.5266)   

#print(f"Valor1 = {valor1:10d}; \nValor2 = {valor2:10d}; \nValor3 = {valor3:10d}. ")

    #usamos o (. f) caso queira representar o numero real (float) com suas casas decimais, mesmo quando não possui valor
    
    #como os valores foram transformados em int(), não obtemos nada nas casas decimais mesmo representando elas no print. 

    #usamos tambêm o (: d) para representar em quantos bits o valor sera mostrado apenas sem suas casas decimais após o int() 


print(f"Valor1 = %f; \nValor2 = %d; \nValor3 = %o."  % (valor1, valor2, valor3))

    #Utilizar % (lista dos valores), e após isso, onde a formula encontrar %d irá colocar os valores em ordem.
    #NOMENCLATURAS APRENDIDAS
    # f = float ou seja número real
    # d = int = Inteiro ou seja mostra o número inteiro sem decimal
    # o = base octal ou seja converte o número de base decimal para base octal (apenas funciona com números inteiros)