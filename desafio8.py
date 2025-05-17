valor = int(input("Insira o primeiro valor: "))
valor2 = int(input("Insira o segundo valor: "))
calc = input("aperte + para somar, - para subtrair, * para multiplicação e / para divisão: ")

def soma(a,b):
    resultado = a+b
    print(f"O resultado é {resultado}")

def subtração(a,b):
    resultado = a-b
    print(f"O resultado é {resultado}")

def multiplicação(a,b):
    resultado = a*b
    print(f"O resultado é {resultado}")

def divisão(a,b):
    resultado = a/b
    print(f"O resultado é {resultado}")

if(calc == "+"):
    soma(valor,valor2)
elif(calc == "-"):
    subtração(valor,valor2)
elif(calc == "*"):
    multiplicação(valor,valor2)
elif(calc == "/"):
    if(valor == 0 or valor2 == 0):
        print("Não é possível dividir por 0.")
    else:
        divisão(valor,valor2)
else:
    print("Operador inválido.")