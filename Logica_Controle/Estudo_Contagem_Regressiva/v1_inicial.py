print('bem vindo ao progrma de contagem regressiva')

n = int(input('de onde a contagem deve começar? '))

if n >= 0:
  def contagem_regressiva(n):
    while n >= 0:
      print(n)
      n -= 1
      
  contagem_regressiva(n)
else:
  print('numero invalido, por favor insira um numero maior que 0!')