def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

print("Calculadora Básica em Python")

while True:
    print("\nOperações disponiveis:")
    print("1-Somar")
    print("2-Subtrair")
    print("3-Multiplicar")
    print("4-Dividir")
    print("0-Sair")

    escolha = input("Escolha a operação: ").strip()

    if escolha == '0':
        print("Encerrando a calculadora.")
        break

    try:
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: "))
    except ValueError:
        print("Entrada inválida! Use apenas números.")
        continue

    if escolha == '1':
        print("Resultado:", somar(num1, num2))
    elif escolha == '2':
        print("Resultado:", subtrair(num1, num2))
    elif escolha == '3':
        print("Resultado:", multiplicar(num1, num2))
    elif escolha == '4':
        print("Resultado:", dividir(num1, num2))
    else:
        print("Operação inválida.")
