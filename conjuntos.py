import os

def verificar_conjuntos(conjuntoA,conjuntoB):
    verificador = 0
    for i in conjuntoA:
        if i in conjuntoB:
            verificador +=1
    if verificador == len(conjuntoA) and not conjuntoA == conjuntoB:
        print("\nA É subconjunto PRÓPRIO de B")
    else:
        print("\nA NÃO é subconjunto PRÓPRIO de B")
    
def uniao_conjuntos(conjuntoA,conjuntoB):
    uniao = []
    uniao = conjuntoA + conjuntoB
    for i in conjuntoA:
        if i in conjuntoB:
            uniao.remove(i)
    print(f"\nA união entre os conjuntos A e B é igual a: {sorted(uniao)}\n")

def intersecao(conjuntoA,conjuntoB):
    intersecao_A_B = []
    for i in conjuntoA:
        if i in conjuntoB:
            intersecao_A_B.append(i)
    print(f"A intersecao entre A e B é igual a: {sorted(intersecao_A_B)}\n")

def diferenca(conjuntoA,conjuntoB):
    diferenca_A_B = []
    for i in conjuntoA:
        if i not in conjuntoB:
            diferenca_A_B.append(i)
    for i in conjuntoB:
        if i not in conjuntoA:
            diferenca_A_B.append(i)
    print(f"A diferença entre A e B é igual a: {sorted(diferenca_A_B)}\n")

def main_conjuntos():
    conjuntoA = []
    conjuntoB = []

    os.system("cls")
    tamConjuntoA = int(input("\nDigite a quantidade de números do conjunto A: "))
    contador_A = 0
    while contador_A != tamConjuntoA:
        num = int(input(f"Insira o {contador_A +1}° número: "))
        if num in conjuntoA:
            print("\nErro! Este número já foi digitado\n")
            continue
        conjuntoA.append(num)
        contador_A +=1

    os.system("cls")
    tamConjuntoB = int(input("\nDigite a quantidade de números do conjunto B: "))
    contador_B = 0
    while contador_B != tamConjuntoB:
        num = int(input(f"Insira o {contador_B +1}° número: "))
        if num in conjuntoB:
            print("\nErro! Este número já foi digitado\n")
            continue
        conjuntoB.append(num)
        contador_B +=1

    os.system("cls")
    print(f"\nConjunto A: {sorted(conjuntoA)}\nConjunto B: {sorted(conjuntoB)}\n")
    verificar_conjuntos(conjuntoA,conjuntoB)
    uniao_conjuntos(conjuntoA,conjuntoB)
    intersecao(conjuntoA,conjuntoB)
    diferenca(conjuntoA,conjuntoB)








    
         

   
