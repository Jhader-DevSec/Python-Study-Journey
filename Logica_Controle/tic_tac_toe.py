import random

lista_jogadas = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numeros_jogados = []
combinacoes = [(1, 2 , 3), (4, 5, 6), (7, 8, 9), (1 , 4, 7), (2, 5, 8), (3, 6, 9), (7 , 5, 3), (1, 5, 9)]

def mostrar_tabuleiro():
    print(
        f"{lista_jogadas[1]} | {lista_jogadas[2]} | {lista_jogadas[3]}\n" 
        f"{lista_jogadas[4]} | {lista_jogadas[5]} | {lista_jogadas[6]}\n" 
        f"{lista_jogadas[7]} | {lista_jogadas[8]} | {lista_jogadas[9]}\n"
    )


def atualizar_tabuleiro_maquina(jogada):
    global lista_jogadas
    lista_jogadas[jogada] = "X"

def atualizar_tabuleiro_jogador(jogada):
    global lista_jogadas
    lista_jogadas[jogada] = "O"
    numeros_jogados.append(jogada)

def jogada_maquina():
    global lista_jogadas
    global numeros_jogados

    available_positions = [i for i in range(1, 10) if isinstance(lista_jogadas[i], int)]

    if not available_positions: 
        return False 

    jogada = random.choice(available_positions)
    numeros_jogados.append(jogada)
    atualizar_tabuleiro_maquina(jogada)
    return True 

def verificar_vitoria():
    global combinacoes
    for c in combinacoes:
      p1 , p2, p3 = c
      if lista_jogadas[p1] == lista_jogadas[p2] == lista_jogadas[p3]:
        print(f"O jogador {lista_jogadas[p1]} venceu!") 
        return True
    return False



while True:
  mostrar_tabuleiro()

  jogada_jogador_str = input("Digite a jogada: ")
  if not jogada_jogador_str.isdigit():
    print("Por favor, digite um número válido.")
    continue
  jogada_jogador = int(jogada_jogador_str)

  if not (1 <= jogada_jogador <= 9) or not isinstance(lista_jogadas[jogada_jogador], int):
    print("Posição inválida ou já ocupada. Tente novamente.")
    continue

  atualizar_tabuleiro_jogador(jogada_jogador)

  if verificar_vitoria():
    mostrar_tabuleiro()
    print("Fim de jogo!")
    break

  if len(numeros_jogados) == 9: 
      mostrar_tabuleiro()
      print("Empate!")
      break

  if jogada_maquina(): 
      if verificar_vitoria():
        mostrar_tabuleiro()
        print("Fim de jogo!")
        break
  
  if len(numeros_jogados) == 9: 
      mostrar_tabuleiro()
      print("Empate!")
      break