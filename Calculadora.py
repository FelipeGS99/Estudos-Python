from math import sqrt
def conta(n1, op, n2):
    if op == "+":
        resultado = float(n1 + n2)
        print("O resultado da soma entre {} e {} é: {}".format(n1, n2, resultado))
    elif op == "-":
        resultado = float(n1 - n2)
        print("O resultado da subtração entre {} e {} é: {}".format(n1, n2, resultado))
    elif op == "/":
        resultado = float(n1 / n2)
        print("O resultado da divisão entre {} e {} é: {}".format(n1, n2, resultado))
    elif op == "*":
        resultado = float(n1 * n2)
        print("O resultado da multiplicação entre {} e {} é: {}".format(n1, n2, resultado))
    else:
        print("Operador inválido.")
        resultado = None
    return resultado


n1 = float (input())
op = str (input())
if op == "sqrt":
    resultado = float(sqrt(n1))
    print("A raiz quadrada de {} é igual a: {:.2f}".format(n1, resultado))
else:
    n2 = float (input())
    resultado = conta(n1, op, n2)





