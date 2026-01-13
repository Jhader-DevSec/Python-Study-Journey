senha = 'sou o proximo hacker'
tentativas = 5

while tentativas > 0:
  tentativa_senha = input('digite a senha')
  if tentativa_senha == senha:
    print('voce tem acesso ao sistema')
    break
  else:
    tentativas -= 1
    print(f'voce errou, lhe restam apenas {tentativas}')
else:
  print('voce nao tem mais tentativas')