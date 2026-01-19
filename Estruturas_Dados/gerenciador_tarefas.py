def main():

  tarefas = []

  print('-----Bem vindo a lista de tarefas!-----')

  while True:
    print('\n-----\nO que voçe deseja fazer?-----')
    print('1 - Adicionar tarefa')
    print('2 - Listar tarefas')
    print('3 - remover tarefa')
    print('4 - sair')

    try:
      opcao = int(input('Digite a opção desejada: '))
    except ValueError:
      print('Por favor, utilize apenas números para a opção!')
      continue

    if opcao not in (1, 2, 3, 4):
      print('Opção inválida! Por favor, escolha entre 1, 2, 3 ou 4.')
      continue

    if opcao == 1:
      tarefa = input('Digite a tarefa: ')
      tarefas.append(tarefa)
      print('Tarefa adicionada com sucesso!')

    elif opcao == 2:
        print('\n-----Tarefas-----')

        if len(tarefas) == 0:
            print('Sua lista está vazia')

        else:
            for i, tarefa in enumerate(tarefas):
                print(f'{i + 1}. {tarefa}')

    elif opcao == 3:
        print('\n-----Remover Tarefas-----')

        if len(tarefas) == 0:
            print('Sua lista de tarefas está vazia. Nada para remover.')
            continue

        for i, tarefa in enumerate(tarefas):
            print(f'{i + 1}. {tarefa}')

        try:
            tarefa_remover = int(input('Digite o número da tarefa que deseja remover: '))
            valor = tarefa_remover - 1

            if 0 <= valor < len(tarefas):
                tarefas.pop(valor)
                print('Tarefa removida com sucesso!')
            else:
                print('Número de tarefa inválido!')

        except ValueError:
            print('Por favor, utilize somente números para indicar a tarefa!')

    else:
        print('Até logo!')
        break

if __name__ == "__main__":
    main()