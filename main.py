import os, sys, time
from conjuntos import main_conjuntos

def menu():
    while True:
        menu = int(input("\nEscolha uma opção da calculadora:\n1- Funções\n2- Conjuntos\n3- Matrizes\n4- Sair\n\n-> "))
        return menu

os.system("cls")
print("-"*30, " Calculadora RMC ", "-"*30)
while True:
    escolha = menu()
    #FUNÇÕES
    if escolha == 1:
        while True:
            os.system("cls")
            print("-"*30, " Calculadora RMC ", "-"*30, "\nEscolheu Funções")
            qual_funcao = int(input("\n1- Função do 1º grau\n2- Função do 2º grau\n\n-> "))

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

