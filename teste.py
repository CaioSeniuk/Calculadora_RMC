'''def calcular_raizes(a, b, c):
    # calcula o discriminante
    d = (b**2) - (4*a*c)

    # verifica se o discriminante é negativo
    if d < 0:
        print("A função não retornou um objeto iterável.")

    # calcula as raízes
    raiz1 = (-b - d**(1/2))/(2*a)
    raiz2 = (-b + d**(1/2))/(2*a)

    return raiz1, raiz2

# teste do código
a = 1
b = 2
c = -3

raiz1, raiz2 = calcular_raizes(a, b, c)

if raiz1 and raiz2:
    print("As raízes da equação são:", raiz1, raiz2)
else:
    print("A equação não tem raízes reais.")'''

import matplotlib.pyplot as plt
import numpy as np
import math

def calcular_raizes(a, b, c):
    #CALCULAR O DELTA
    d = (b**2) - (4*a*c)

    #CALCULAR AS RAIZES
    if d >= 0:
        raiz1 = (-b - math.sqrt(d))/(2*a)
        raiz2 = (-b + math.sqrt(d))/(2*a)
        print(f"\nAs raízes da equação são: {raiz1:.2f} e {raiz2:.2f}")
    else:
        raiz1 = -b/(2*a)
        raiz2 = math.sqrt(-d)/(2*a)
        print(f"\nAs raízes da equação são: {raiz1:.2f} + {raiz2:.2f}i e {raiz1:.2f} - {raiz2:.2f}i")

def xvertice(a,b):
    xv = -(b/(2*a))
    return xv

def yvertice(a,b,c):
    d = (b**2)
    yv = -(d-(4*a*c))/ (4*a)
    return yv

def f(a,b,c,x):
        y = a*((x)*(x)) + b*x + c; return y
while True:
    print("\nFunção 2º Grau f(x) = ax² + bx + c, o parâmetro de x será determinado por você - Digite 000 para Sair")
    a = int(input("\nInsira o valor de a: "))
    if a == 000:
        break
    b = int(input("\nInsira o valor de b: "))
    if b == 000:
        break
    c = int(input("\nInsira o valor de c: "))
    if c == 000:
        break
    x = int(input("\nInsira um parametro de X: "))
    if x == 000:
        break

    #VALOR A SER CALCULADO EM F(X)
    fx = x
    #VALOR QUE SERÁ UTILIZADO COMO PARÂMETRO PARA O EIXO Y
    fx_calculado = f(a,b,c,x)

#Definindo parâmetros de -10 até 10 de 1 em 1
    eixoX =  np.arange(-10,11,1) 
    eixoY = []
    for x in eixoX:
        y = f(a,b,c,x)
        eixoY.append(y)

#CALCULAR O VÉRTICE
    xVertice = xvertice(a,b)
    yVertice = yvertice(a,b,c)

#CALCULAR RAIZES
    calcular_raizes(a,b,c)
    print(f"\nf({fx}) = {fx_calculado}")

    #PARA VALOR MÍNIMO
    if a>0:
        plt.plot(eixoX, eixoY, label = f"f(x) = {a}x² + {b}x + {c}", color = "b")
        plt.title(f"Função f({fx}) = {a}x² + {b}x + {c} \n Com valor mínimo em ({xVertice}, {yVertice}) \n xV = {xVertice} , yV = {yVertice}")
        plt.xlabel("eixo X")
        plt.ylabel("eixo y")
        plt.grid(True)
        plt.axhline(y=0, color = "k")
        plt.axvline(x=0, color = "k")
        plt.plot(xVertice,yVertice,fx,fx_calculado, marker = "o")
        plt.show()
        break

    #PARA VALOR MÁXIMO
    elif a < 0:
        plt.plot(eixoX, eixoY, label = f"f(x) = {a}x² + {b}x + {c}", color = "b")
        plt.title(f"Função f({fx}) = {a}x² + {b}x + {c} \n Com valor máximo em ({xVertice}, {yVertice}) \n xV = {xVertice} , yV = {yVertice}")
        plt.xlabel("eixo X")
        plt.ylabel("eixo y")
        plt.grid(True)
        plt.axhline(y=0, color = "k")
        plt.axvline(x=0, color = "k")
        plt.plot(xVertice, yVertice, fx, fx_calculado, marker = "o")
        plt.show()
        break