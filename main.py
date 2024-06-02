import os, sys, time
from conjuntos import main_conjuntos
from funcao_1_grau import funcao_1grau
from funcao_2_grau import funcao_2grau

def menu():
    menu = int(input("\nEscolha uma opção da calculadora:\n1- Funções\n2- Conjuntos\n3- Matrizes\n4- SAIR\n\n-> "))
    return menu

while True:
    os.system("cls")
    print("-"*30, " Calculadora RMC ", "-"*30)
    escolha = menu()
    #FUNÇÕES
    if escolha == 1:
        while True:
            os.system("cls")
            print("-"*30, " Calculadora RMC ", "-"*30, "\nEscolheu Funções")
            qual_funcao = int(input("\n1- Função do 1º grau\n2- Função do 2º grau\n3- SAIR\n\n-> "))
            
            if qual_funcao == 1:
                funcao_1grau()
                break
            elif qual_funcao == 2:
                funcao_2grau()
                break
            elif qual_funcao == 3:
                break
            else:
                print("\nErro! Insira um valor válido...")
                time.sleep(1)
                continue

    #CONJUNTOS
    elif escolha == 2:
        main_conjuntos()
        continue
    
    #MATRIZES
    elif escolha == 3:
        print("\nEscolha 3")

    #SAIR
    elif escolha == 4:
        print("\nSaindo...\n\n"), time.sleep(1), os.system("cls")
        break

    #CONDIÇÃO PARA EVITAR ERRO
    else: 
        print("\nErro! Insira um valor válido...\n")
        continue

