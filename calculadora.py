"""

calculos básicos somar,subtrair,dividir,multiplicar.
com um MENU utilizando condições de if, else sendo queo usuário escolha qual função deve acessar.
colhido a função , o usuário é direcionado a ela e insere os parâmetros que desejam realizar as operações.
as funições matemáticas receberem os números para realizar a operação, realizar o cálculo e imprimir o resultado para o usuário.
"""
def somar(a, b):
    soma = a + b
    return print(f"O resultado da soma é: {soma}")

def subtrair(a, b):
    sub = a - b
    return print(f"O resultado da subtração é: {sub}")

def dividir(a, b):
    dividir = a / b
    return print(f"O resultado divisão é: {dividir}")

def multiplicar(a, b):
    multiplicar = a * b
    return print(f"O resultado multiplicação é:  {multiplicar}")



def calcular():
    print("#--------------------------------------------------------#")
    print("#---------Escolha a operação que deseja realizar---------#")
    print("#--------------------------------------------------------#")
    print("[1] - Somar")
    print("[2] - Subtrair")
    print("[3] - Dividir")
    print("[4] - Multiplicar")
    print("[5] - Para Sair do sistema")
    
    
    try:
        escolha = int(input("Esolha uma opção do menu: "))
        if escolha != 5 and escolha < 5:
            a = int(input("Digite o primeiro valor: "))
            b = int(input("Digite o segundo valor: "))
        
    except Exception as e:
        print("Opção inválida.")
        calcular()
    
    if escolha == 1:
        somar(a, b)
        calcular()
    elif escolha == 2:
        subtrair(a, b)
        calcular()   
        
    elif escolha == 3:
        if a != 0 and b != 0:
            dividir(a, b)
            calcular()
        else:
            print("Não podemos efetuar divisão com zero. Tente com outro número!")
            calcular() 
    elif escolha == 4:
        multiplicar(a, b)
        calcular() 
    elif escolha == 5:
        exit()
    else:
        print("Opção Inválidação!")
        calcular()
        
        
if __name__ == "__main__":
    
    calcular()
