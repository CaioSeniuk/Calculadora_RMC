def GerarMatrizes():   
    import time,os,sys
    while True:
        def gerarMatriz(num_linhas, num_colunas):
            matriz = []
            #criar um for para linhas
            for i in range(num_linhas):
                linha = []
                #Quantas colunas serão geradas, assim como os número das linhas serão preenchidos
                for X in range(num_colunas): 
                    num_digitado = float(input("\nInsira um número: "))
                    #armazeno na lista linha um numero aleatorio
                    linha.append(num_digitado)
                #armazeno em matriz a lista linha, PRECISO DE VARIAS LISTAS EM UMA LISTA PARA SER UMA MATRIZ 
                matriz.append(linha) 
            return matriz
        os.system("cls")
        print("-"*30, " Calculadora RMC ", "-"*30, "\nEscolheu Matrizes")
        print("\nO programa só poderá ser parado no primeiro input, digite -1 para sair\n")
        linhas = int(input("Informe o numero de linhas da matriz: "))
        if linhas == -1:
            break
        colunas = int(input("Informe o numero de colunas da matriz: "))
        if colunas == -1:
            break

        elif linhas<-1 or linhas == 0:
            print("\nErro! Insira um valor válido...\n")
            time.sleep(2)
            continue
        elif colunas<-1 or linhas == 0:
            print("\nErro! Insira um valor válido...\n")
            time.sleep(2)
            continue
        matriz = gerarMatriz(linhas,colunas)

    #LOOPING PARA IMPRIMIR NA TELA A MATRIZ
        print("-="*30,"\n" )
        for l in range(0,linhas):
            for c in range(0,colunas):
                print(f"[{matriz[l][c]:^5}]", end="")
            print()#pular linha pra ficar "bonito"
        print()#pular linha pra ficar "bonito"
        escolha = int(input("\nPara voltar ao menu Principal digite qualquer número (menos o -1)\nPara sair da Calculadora digite -1\n\n--> "))
        if escolha == -1:
            sys.exit()
        else:
            break