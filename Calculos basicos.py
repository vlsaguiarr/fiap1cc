denominante = input("Qual operação será realizada? \n \n 1) delta \n 2) media \n 3) porcentagem \n 4) proximo multiplo \n 5) saque financeiro \n 6) conversão em base 16 \n 7) conversão para a base 8 \n")

# Calcule a média
if denominante == str("1" or "delta"):
    #ler o valor da média 1
    m1 = int(input("Coloque o primeiro valor: "))
    #ler o valor da média 2
    m2 = int(input("Coloque o segundo valor: "))
    #ler o valor da média 3
    m3 = int(input("Coloque o terceiro valor: "))
    #calcular a média
    media = (m1 + m2 + m3) / 3
    #exibir a média
    print(f"A média dos números {m1}, {m2} e {m3} é: {media:.1f}")

#Calcule o delta, dado os valores do usuario
#entrada = 1, 2 e 3     saida = -8
#entrada = -1, 2 e 3    saida = 16

if denominante == str("2" or "media"):
    #ler o valor de A
    print("calculo do delta")
    a = int(input("Digite o valor de A: "))
    #ler o valor de B
    b = int(input("Digite o valor de B: "))
    #ler o valor de C
    c = int(input("Digite o valor de C: "))
    #calcular o delta
    delta = b ** 2 - 4 * a * c
    #exibir o delta
    print(f"O valor do Delta é: {delta:.2f}")

#Calcular porcentagem
#Calculo = VALOR * percentual / 100
# 100% equivale a 1
# 20% equivale a 0.2

if denominante == str("3" or "porcentagem" or "porce"):
    # saber se a operação é um desconto ou acrescento
    denominar = input("Esta operação é (em números): \n 1) acrescimo \n 2) desconto \n 3) saber a porcentagem\n")
    # saber o valor
    valor = int(input("Digite o valor : "))
    # saber a porcentagem
    por = int(input("Qual a porcentagem desejada (em números):"))
    decimo = por / 100
    # realizar o calculo

    if denominar == str("1"):

        resultado = valor * (1 + decimo)
        # exibir a porcentagem
        print(f"O acrescimo de {por}% em {valor} é: {resultado:.2f} \nPois {por}% de {valor} é {resultado - valor:.2f} ")



    if denominar == str("2"):

        resultado = valor * (1 - decimo)
        #exibir mensagem
        print(f"O desconto de {por}% em {valor} é: {resultado:.2f} \nPois {por}% de {valor} é {resultado + valor:.2f} ")

    if denominar == str("3"):

        resultado = valor - (valor *(1 - decimo))
        #exibir a mensagem
        print(f"{por}% de {valor} é: {resultado:.2f}")

#Calcule o proximo multiplo de x

if denominante == str("4" or "multiplo" or "prox"):
    #ler o número do usuario
    num = int(input("Digite o valor: "))
    #pegar o multiplo
    mul = int(input("Digite o multiplo: "))
    #calcular o proximo multiplo de x
    prox_mul = num // mul * mul + mul
    #exibir
    print(f"o proximo multiplo de {mul} a partir de {num} é: {prox_mul:.2f}")

# Saque financeiro

if denominante == str("5" or "saque"):
    #receber o valor
    valor_total = int(input("Qual a quantia você deseja sacar?"))
    sim = input(f"você tem certeza que deseja sacar {valor_total}R$? \n s/n")

    if sim == str("n"):
        print("tenta dnv")

    # calcular a quantidade de cédulas de 100
    if sim == str("s"):
        valor = valor_total
        cem = valor % 100
        cedulascem = valor // 100
        #atualizar a quantia
        valor = cem
        # calcular a quantidade de cédulas de 50
        cinquenta = valor % 50
        cedulacinco = valor // 50
        # atualizar a quantia
        valor = cinquenta
        # calcular a quantidade de cédulas de 20
        vinte = valor % 20
        cedulavinte = valor // 20
        # atualizar a quantia
        valor = vinte
        # calcular a quantidade de cédulas de 10
        dez = valor % 10
        ceduladez = valor // 10
        # atualizar a quantia
        valor = dez
        print(f"Você sacou {valor_total}R$ em \n"
              f"{cedulascem}  cédulas de 100, \n"
              f"{cedulacinco} cédulas de 50, \n"
              f"{cedulavinte} cédulas de 20, \n"
              f"{ceduladez}   cédulas de 10!")



#Conversão para base 16

if denominante == str("6" or "base 16"):
        resultado = input("conversão de 16 para 10? s/n")
        if resultado == str("s"):
            hexdec = input("Digite o valor em hexadecimal: ")
            hexdec2 = int(hexdec, 16)
            print(f"O número {hexdec} em base decimal: {hexdec2}")

        if resultado == str("n"):
            conversao = input("Digite o número na base 10:")
            conversao = int(conversao)
            print(f"O número {conversao} na base 16(hex) equivale a:", hex(conversao))


#Conversão para base 8

if denominante == str("7" or "base 8"):
        conversao = input("Digite o número na base 10:")
        conversao = int(conversao)


        print("O número %d na base 8 equivale a: %o" % (conversao, conversao))