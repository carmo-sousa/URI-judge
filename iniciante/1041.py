#!/usr/bin/python3
"""
===============================================================================
PROBLEMA: 1041
NÍVEL: Inciante
DATA DE SUBMISSÃO:
===============================================================================
Coordenadas de um ponto

Leia 2 valores com uma casa decimal (x, y), que devem representar
as coordenadas de um ponto em um plano. A seguir, determine qual o
quadrante ao qual pertence o ponto, ou se está sobre um dos eixos
cartesianos ou na origem (x=0 y=0).

    y
 Q2 | Q1
----+---- x
 Q3 | Q4

Se o ponto estiver na origem, escreva a mensagem "Origem".
Se o ponto estiver sobre um dos eixos escreva "Eixo X" ou "Eixo Y", conforme
for a situação.

===============================================================================
ENTRADA

A entrada contem as coordenadas de um ponto.

===============================================================================
SAÍDA

A saída deve apresentar o quadrante em que o ponto se encontra.
===============================================================================

+-------------------------------+-------------------+
| Exemplo de Entrada            | Exemplo de Saída  |
+-------------------------------+-------------------+
| 4.5 -2.2                      | Q4                |
+-------------------------------+-------------------+
| 0.1 0.1                       | Q1                |
+-------------------------------+-------------------+
| 0.0 0.0                       | Origem            |
+-------------------------------+-------------------+

===============================================================================
"""

# Q1 = ( x,  y)
# Q2 = (-x,  y)
# Q3 = (-x, -y)
# Q4 = ( x, -y)

coordinates = input()
coordinates = coordinates.split(' ')

x_axis = float(coordinates[0])
y_axis = float(coordinates[1])

if x_axis == 0 and y_axis == 0:
    print('Origem')

elif x_axis == 0:
    print('Eixo X')

elif y_axis == 0:
    print('Eixo Y')

elif x_axis > 0 and y_axis > 0:
    print('Q1')

elif x_axis < 0 and y_axis > 0:
    print('Q2')

elif x_axis < 0 and y_axis < 0:
    print('Q3')

elif x_axis > 0 and y_axis < 0:
    print('Q4')
