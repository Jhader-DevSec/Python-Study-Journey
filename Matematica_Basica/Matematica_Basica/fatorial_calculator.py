def fatorial(x):
    if x == 0:
        return 1
    return x * fatorial(x - 1)

# Recebe o número do usuário
numero = int(input("Digite um número para calcular o fatorial: "))
resultado = fatorial(numero)
print(f"O fatorial de {numero} é {resultado}")
