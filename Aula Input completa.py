#Saida de dados: interação do sistema com o usuário  -> Print
#Entrada de dados: interação do usuário com o sistema -> Input

#valor = input ("Digite um valor: ")

#print(valor)


    #o comando ira pedir para o usuario "digite um valor:", e após o usuário digitar, ira inputar o valor na variavel e prosseguir com o comando print(valor).

# se quisessemos realizar uma operação de dobrar o valor por exemplo, realizariamos o seguinte comando:

#valor = input ("Digite um valor: ")
#resposta = valor+valor 

#print("Resultado ; ", resposta)

    #Nesse caso, o sinal "+" realiza a junção de dois conteudos de texto, então a resposta apenas juntaria dois valores de input (edson) ou seja (edsonedson)
    #No caso, se nós colocarmos input(), o comando ira entender a resposta como um valor textual e não numérico, para isso usamos :

#valor = input("Digite um valor:")
#valor = int(valor)
    #isso faz com que o valor agora seja interpretado como um número inteiro
#resposta = valor + valor

#print("Resultado: ", resposta)

#Agora irei realizar a representação do calculo do dobro, porém com mais uma linha para mostrar ao usuario dados.

# Usuário digita um valor
#valor = input("Digite um valor:")
# Mostra o valor e o tipo
#print(valor, type(valor))
# Converte o valor para inteiro
#valor = int(valor)
# Realiza o calculo do dobro
#resposta = valor + valor
# Mostra a resposta
#print("Resultado: ", resposta)

    # neste caso, o type vai identificar qual a classificação desse dado obtido, que no caso, ainda não foi convertido para um número inteiro, então sera identificado como "str" = texto
    # então para melhor realização inverterei os passos:

# Usuário digita um valor
#valor = input("Digite um valor:")
# Mostra o valor e o tipo
#print(valor, type(valor))
# Converte o valor para inteiro
#valor = int(valor)
# Mostra o valor e o tipo
#print(valor, type(valor))
# Realiza o calculo do dobro
#resposta = valor + valor
# Mostra a resposta
#print("Resultado: ", resposta)

#Uma maneira diferente de realizar esse algoritmo

# Solicita ao usuario o valor e o classifica como inteiro
#valor = int(input("Digite um valor:"))
# Mostra o valor e o tipo
#print (valor, type(valor))
# Realiza o calculo
#resposta = valor + valor
# Mostra o resultado 
#print("Resultado: ", resposta)

# Para simplificar, podemos realizar o calculo diretamente no comando print.
# A situação se resume em:
    # Usaremos esse comando novamente no algoritmo?
        #Sim -> jogue em uma variavel 
        #Não -> podemos simplificar no print

# Caso precisamos realizar operações com números fracionados, utilizamos o casting float :

valor = float(input("Digite um valor:"))
print(valor, type(valor))
print("Resultado: ", valor + valor)