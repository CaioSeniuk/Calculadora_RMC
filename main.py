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
    if escolha == 2:
        main_conjuntos()
        continue
    elif escolha == 4:
        print("\nSaindo...\n\n")
        time.sleep(1)
        os.system("cls")
        break

