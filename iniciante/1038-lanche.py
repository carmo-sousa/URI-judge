#!/bin/python3

"""
===============================================================================
PROBLEMA: 1038
NÍVEL: Fácil
DATA DE SUBMISSÃO: 17/06/20

===============================================================================
Com base na tabela abaixo, escreva um programa que leia
o código de um item e a quantidade deste item. A seguir,
calcule e mostre o valor da conta a pagar.

+------------+-------------------+--------+
|CÓDIGO      | ESPECIFICAÇÃO     | PREÇO  |
+------------+-------------------+--------+
|1           | Cachorro Quente   | R$ 4.00|
|2           | X-Salada          | R$ 4.50|
|3           | X-Bacon           | R$ 5.00|
|4           | Torrada simples   | R$ 2.00|
|5           | Refrigerante      | R$ 1.50|
+-----------------------------------------+

===============================================================================
ENTRADA

O arquivo de entrada contém dois valores
inteiros correspondentes ao código e à
quantidade de um item conforme tabela acima.

===============================================================================
SAÍDA

O arquivo de saída deve conter a mensagem
"Total: R$" seguido pelo valor a ser pago,
com 2 casas após o ponto decimal.

===============================================================================
Exemplo de entrada          Exemplo de saída
3 2                         Total: R$ 10.00
4 3                         Total: R$ 6.00
2 3                         Total: R$ 13.50
===============================================================================

"""

# código e preço
menu = [
    [1, 4.0],
    [2, 4.5],
    [3, 5.0],
    [4, 2.0],
    [5, 1.5]
    ]

request = input()
request = request.split(' ')

item_code = int(request[0])
qtd = int(request[1])

total = qtd * menu[item_code - 1][1]

print('Total: R$ {:.2f}'.format(total))
