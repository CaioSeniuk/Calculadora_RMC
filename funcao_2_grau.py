def funcao_2grau():   
    import numpy as np #pip install
    import matplotlib.pyplot as plt

    def f(a,b,c,x):
        y = a*((x)*(x)) + b*x + c; return y
    while True:
        print("\nFunção 2º Grau f(x) = ax² + bx + c, os parâmetros de x serão determinados por você - Digite 000 para Sair")
        a = int(input("\nInsira o valor de a: "))
        if a == 000:
            break
        b = int(input("\nInsira o valor de b: "))
        if b == 000:
            break
        c = int(input("\nInsira o valor de c: "))
        if c == 000:
            break
        x1 = int(input("\nInsira o primeiro parametro de X: "))
        if x1 == 000:
            break
        x2 = int(input("\nInsira o segundo parametro de X: "))
        if x2 == 000:
            break

        eixoX = [x1,x2]
        #eixoX =  np.arange(-10,10,1) #do -1o até 10 em parametro de 1 em 1
        eixoY = []
        for x in eixoX:
            y = f(a,b,c,x); eixoY.append(y)

        plt.plot(eixoX, eixoY, label = f"f(x) = {a}x² + {b}x + {c}", color = "b")
        plt.title(f"Função f(x) = {a}x² + {b}x + {c}")
        plt.xlabel("eixo X")
        plt.ylabel("eixo y")
        plt.grid(True)
        plt.axhline(y=0, color = "k")
        plt.axvline(x=0, color = "k")
        plt.show()
        break