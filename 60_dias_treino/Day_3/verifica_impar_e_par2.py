entrada = input("Coloque o numero: ")

try:
    numero = int(entrada)
    if numero % 2 == 0:
        print("Numero par")
    else:
        print("Numero impar")
except ValueError:
    print("Voce nao passou um numero inteiro")