print("bem vindo a calculadora do DEV!")

while True:
    operação = input("digite a operação (+, -, *, /): ")
    if operação in  '+-*/':
        num1 = float(input("digite um numero: "))
        num2 = float(input("digite outro numero: "))
        if operação == "+":
            resultado = num1 + num2
            print(f"o resultado de seu calculo é: {resultado}")
        elif operação == "-":
            resultado = num1 - num2
            print(f"o resultado de seu calculo é: {resultado}")
        elif operação == "*":
            resultado = num1 * num2
            print(f"o resultado de seu calculo é: {resultado}")
        elif operação == "/":
            if num2 == 0:
                print("erro: não é permitido dividir por zero.")
            else:
                resultado = num1 / num2
            print(f"o resultado de seu calculo é: {resultado}")
    else:
            print("operação invalida. Por favor, escolha entre +, -, * ou /.")

    continuar = input("Deseja realizar outra operação? (s/n): ")

    if continuar.lower() == 'n':
            print("Encerrando a calculadora. Até a próxima!")

            break
