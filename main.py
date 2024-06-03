import os, sys, time
from conjuntos import main_conjuntos
from funcao_2_grau import funcao_2grau
from funcao_exponencial import funcao_exp

def menu():
    menu = int(input("\nEscolha uma opção da calculadora:\n1- Conjuntos\n2- Função 2º Grau\n3- Função exponencial\n4- Matrizes\n5- SAIR\n\n-> "))
    return menu

while True:
    os.system("cls")
    print("-"*30, " Calculadora RMC ", "-"*30)
    escolha = menu()

    #CONJUNTOS
    if escolha == 1:
        main_conjuntos()
        continue

    #FUNÇÃO 2º GRAU
    elif escolha == 2:
        funcao_2grau()
        continue

    #FUNÇÃO EXPONENCIAL
    elif escolha == 3:
        funcao_exp()
        continue

    #MATRIZES
    elif escolha == 4:
        print("\nEscolha 4")

    #SAIR
    elif escolha == 5:
        print("\nSaindo...\n\n"), time.sleep(1), os.system("cls")
        break

    #CONDIÇÃO PARA EVITAR ERRO
    else:
        print("\nErro! Insira um valor válido...\n")
        time.sleep(2)
        continue

