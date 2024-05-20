import numpy as np #pip install
import matplotlib.pyplot as plt

def f(a,b,c,x):
    y = a*((x)*(x)) + b*x + c; return y

a = int(input("\nInsira o valor de A: "))
b = int(input("\nInsira o valor de B: "))
x1 = int(input("\nInsira o primeiro parametro de X: "))
x2 = int(input("\nInsira o segundo parametro de X: "))
eixoX = [x1,x2]
c = 1
        
#eixoX =  np.arange(-10,10,1) #do -1o até 10 em parametro de 1 em 1
eixoY = []
for x in eixoX:
    y = f(a,b,c,x); eixoY.append(y)

plt.plot(eixoX, eixoY, label = f"f(x) = {a}x + {b}", color = "b")
plt.title(f"Função f(x) = {a}x² + {b}x + 1")
plt.xlabel("eixo X")
plt.ylabel("eixo y")
plt.grid(True)
plt.axhline(y=0, color = "k")
plt.axvline(x=0, color = "k")
plt.show()