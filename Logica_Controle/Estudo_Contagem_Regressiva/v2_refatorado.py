# 1. Primeiro: Definimos as ferramentas (Função fica fora de tudo o que impede possiveis erros no codigo)
def contagem_regressiva(valor):
    while valor >= 0:
        print(valor)
        valor -= 1

# 2. Segundo: Começa o programa principal
print('bem vindo ao programa...')
n = float(input('de onde a contagem deve começar? '))

# 3. Terceiro: Lógica de decisão
if n >= 0:
    # A função já existe desde o começo, agora só usamos ela
    contagem_regressiva(n) 
else:
    print('numero invalido...')