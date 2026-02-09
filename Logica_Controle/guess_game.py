import random

secret_number = random.randint(0, 100)
chances = 0

print('---BEM VINDO AO ADIVINHE UM NÚMERO---')
print('estou pensando em um número ente 1 e 100')

while True:
    chances += 1
    
    user_guess = int(input('qual numero você acha que é?'))
    
    if user_guess < secret_number:
        print('uhmm parece que o número é mais alto que esse.')
        
    elif user_guess > secret_number:
        print('humm parece que você subiu o valor demais.') 
        
    elif user_guess == secret_number:
        print(f'Parabéns você acertou com {chances} tentativas!')
        break
