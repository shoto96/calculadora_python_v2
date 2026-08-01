import math

def somar(a, b): return a + b
def subtrair(a, b): return a - b
def multiplicar(a, b): return a * b
def dividir(a, b): return "Erro: Divisão por zero." if b == 0 else a / b
def potencia(base, expoente): return math.pow(base, expoente)

def raiz_quadrada(numero):
    return "Erro: Raiz de número negativo." if numero < 0 else math.sqrt(numero)

def fatorial(numero):
    if numero < 0 or not numero.is_integer():
        return "Erro: Fatorial exige inteiro não negativo."
    return math.factorial(int(numero))

def porcentagem(valor, percentual): return (valor * percentual) / 100
def seno(angulo_graus): return math.sin(math.radians(angulo_graus))
def cosseno(angulo_graus): return math.cos(math.radians(angulo_graus))

def tangente(angulo_graus):
    if (angulo_graus - 90) % 180 == 0:
        return "Erro: Tangente indefinida para este ângulo."
    return math.tan(math.radians(angulo_graus))

def exibir_menu():
    print("\n==============================")
    print("      CALCULADORA PYTHON      ")
    print("==============================")
    print("1. Soma (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    print("5. Potenciação (a^b)")
    print("6. Raiz Quadrada (√)")
    print("7. Fatorial (!)")
    print("8. Porcentagem (%)")
    print("9. Seno (sin)")
    print("10. Cosseno (cos)")
    print("11. Tangente (tan)")
    print("0. Sair")
    print("==============================")

def calculadora():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (0-11): ").strip()

        if opcao == "0":
            print("\nSaindo... Até logo!")
            break

        try:
            if opcao in ["6", "7", "9", "10", "11"]:
                num = float(input("Digite o número/ângulo em graus: "))
                if opcao == "6": print(f"\nResultado: √{num} = {raiz_quadrada(num)}")
                elif opcao == "7": print(f"\nResultado: {int(num)}! = {fatorial(num)}")
                elif opcao == "9": print(f"\nResultado: sin({num}°) = {seno(num):.4f}")
                elif opcao == "10": print(f"\nResultado: cos({num}°) = {cosseno(num):.4f}")
                elif opcao == "11": 
                    res = tangente(num)
                    print(f"\nResultado: tan({num}°) = {res if isinstance(res, str) else f'{res:.4f}'}")

            elif opcao in ["1", "2", "3", "4", "5", "8"]:
                if opcao == "8":
                    valor = float(input("Digite o valor principal: "))
                    pct = float(input("Digite a porcentagem (%): "))
                    print(f"\nResultado: {pct}% de {valor} = {porcentagem(valor, pct)}")
                else:
                    num1 = float(input("Digite o primeiro número: "))
                    num2 = float(input("Digite o segundo número: "))
                    if opcao == "1": print(f"\nResultado: {num1} + {num2} = {somar(num1, num2)}")
                    elif opcao == "2": print(f"\nResultado: {num1} - {num2} = {subtrair(num1, num2)}")
                    elif opcao == "3": print(f"\nResultado: {num1} * {num2} = {multiplicar(num1, num2)}")
                    elif opcao == "4": print(f"\nResultado: {num1} / {num2} = {dividir(num1, num2)}")
                    elif opcao == "5": print(f"\nResultado: {num1} ^ {num2} = {potencia(num1, num2)}")

            else:
                print("\n[!] Opção inválida. Tente novamente.")

        except ValueError:
            print("\n[!] Erro: Por favor, digite um número válido.")

if __name__ == "__main__":
    calculadora()
