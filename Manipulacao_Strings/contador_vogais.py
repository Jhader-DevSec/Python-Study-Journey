palavra = input("Qual palavra você quer saber as vogais?")
vogais = "aeiouAEIOU"
contagem = 0

for char in palavra:
    if char in vogais:
        contagem += 1 

print(f"A palavra {palavra} tem um total de {contagem} vogais! ")