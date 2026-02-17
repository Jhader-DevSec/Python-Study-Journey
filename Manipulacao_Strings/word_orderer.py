palavras = input("Digite palavras separadas por vírgula: ")

lista_palavras = [palavra.strip() for palavra in palavras.split(',')]
lista_palavras.sort()

resultado = ','.join(lista_palavras)

print("Palavras ordenadas:", resultado)