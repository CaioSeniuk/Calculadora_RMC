def funcao_exp():   
    import numpy as np
    import matplotlib.pyplot as plt
    import os,time

    def f(a,b,x):
        #forçar o x a ser positivo
        x = abs(x)
        y = a*(b**x)
        return y

    while True:
        os.system("cls")
        print("-"*30, " Calculadora RMC ", "-"*30,"\nFunção exponencial f(x) = ab^x o parâmetro de a,b e x será determinado por você - Digite 505 para Sair")
        print("\nO valor de b não pode ser negativo e nem igual a zero")
        a = float(input("\nInsira o valor de a: "))
        if a == 505:
            os.system("cls")
            break
        b = float(input("Insira o valor de b: "))
        if b == 505:
            os.system("cls")
            break
        elif b<-1 or b == 0:
            print("\nA base não pode ser negativa e nem igual a zero, insira outro valor...")
            time.sleep(4)
            continue
        x = float(input("Insira o valor de x: "))
        if x == 505:
            break

    #VALOR A SER CALCULADO EM F(X)
        fx = x
    #VALOR QUE SERÁ UTILIZADO COMO PARÂMETRO PARA O EIXO Y
        fx_calculado = f(a,b,x)

    #Definindo parâmetros de -10 até 10 de 1 em 1 para o eixo Y
        eixoX =  np.arange(-10,11,1) 
        eixoY = []
        for x in eixoX:
            y = f(a,b,x)
            eixoY.append(y)
        print(f"\nO valor de f(x) é igual a: {fx_calculado:.2f}")

        if b>=1:
                plt.plot(eixoX, eixoY, label = f"f(x) = {a}*{b}^{x}", color = "b")
                plt.title(f"Função f({fx}) = {a}*{b}^{fx}, \nCrescente")
                plt.xlabel("eixo X")
                plt.ylabel("eixo y")
                plt.grid(True)
                plt.axhline(y=0, color = "k")
                plt.axvline(x=0, color = "k")
                plt.show()
                break
        
        elif 0<b<1:
                plt.plot(eixoX, eixoY, label = f"f(x) = {a}*{b}^{x}", color = "b")
                plt.title(f"Função f({fx}) = {a}*{b}^{fx}, \nDecrescente")
                plt.xlabel("eixo X")
                plt.ylabel("eixo y")
                plt.grid(True)
                plt.axhline(y=0, color = "k")
                plt.axvline(x=0, color = "k")
                plt.show()
                break