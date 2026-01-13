idade = input('qual sua idade?')

nome = input('qual seu nome?')
while nome == 'jaguatirica':
    print('somente o dev tem esse nome')
    nome = input('qual seu nome?') 

trabalho = input('qual seu job?')

print(f'olá {nome}, vi que você tem {idade} anos e trabalha com {trabalho}.')