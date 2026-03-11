"""
OPERADORES

OPERADORES DE ATRIBUIÇÃO
= -> x = 3 -> x = 3

+= -> x += 1 -> x = x + 1

-= -> x -= 1 -> x = x - 1

*= -> x *= 2 -> x = x * 2

/= -> x /= 2 -> x = x / 2

%= -> x %= 2 -> x = x % 2

OPERADORES ARITMETICOS
+ -> Adição -> menor prioridade

- -> Subtração


* -> Multiplicação


/ -> Divisão


// -> Divisão inteira


% -> Resto da divisão ou módulo


** -> Exponenciação ou potenciação -> Maior prioridade

OPERADORES RELACIONAIS
== -> Igual -> 5 == 5 -> true

!= -> Diferente -> 5 != 5 -> false

> -> Maior que -> 5 > 5 -> false

< -> Menor que -> 5 < 5 -> false

>= -> Maior igual -> 5 >= 5 -> true

<= -> Menor igual -> 5 <= 5 -> true

OPERADORES LOGICOS
or -> A or B -> ou

and -> A and B -> e

not -> not A -> não

TABELA VERDADE NOT
A   ->  NOT A
True -> False

False -> True

TABELA VERDADE AND
A       ->    B     ->  A and B

False ->    False   -> False

False   ->  True    ->  False

True    ->  False   ->  False

True    ->  True    ->  True

TABELA VERDADE OU
A       ->      B      ->  A or B

False   ->   False     ->  False

False   ->   True      ->  True

True    ->   False     ->  True

True    ->   True      ->  True

OPERADOR DE ASSOCIAÇÃO
in -> "s" in resposta -> true

not in -> "s" not in resposta -> false

Atribuição de operadores
( ) -> Parênteses -> Maior prioridade

** -> Exponenciação


+x, -x -> Sinal


*, /, //, % -> Multiplicação, divisão, divisão inteira e módulo


+, - -> Soma e subtração


<, <=, >, >= -> Relacionais


==, != -> Igual e diferente


is, is not -> Identidade


in, not in -> Associação


not -> Não


and -> E


or -> Ou


=, +=, -=, *=, /=, %= -> Atribuição -> Menor prioridade

id() - retorna o endereço de memoria de um objeto


"""

cidade_p1 = "São Paulo"

cidade_p2 = "São Paulo"

cidade_p3 = "Rio de Janeiro"

print(id(cidade_p1))

print(id(cidade_p2))

print(id(cidade_p3))

print(cidade_p1 is cidade_p2)

print(cidade_p1 is not cidade_p3)

print(cidade_p1 is cidade_p3)