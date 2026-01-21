lista_contatos = {}

def adicionar_contatos(nome, apelido, numero, email):
    lista_contatos[nome] = {
        "apelido": apelido,
        "numero": numero,
        "email": email
    }
    
    print(f'o contato de nome {nome} foi adicionado com sucesso!')
    
def remover_contato(nome):
    visualizar_contatos()
    
    if nome in lista_contatos:
        lista_contatos.pop(nome)
    
        print(f'o contato de nome {nome} foi removido com sucesso!')
        
    else:
        print('o contato procurado nao se encontra na lista!')
        
def modificar_contato(nome):
    if nome in lista_contatos:
        print(f'\n--- Editando: {nome} ---')
        novo_apelido = input('Novo apelido: ').strip()
        novo_numero = input('Novo numero: ').strip()
        novo_email = input('Novo email: ').strip()
        
        
        lista_contatos[nome].update({
            'apelido': novo_apelido, 
            'numero': novo_numero, 
            'email': novo_email
        })
        print(f'\n[*] Dados de {nome} atualizados!')
    else:
        print(f'\n[!] Erro: O contato "{nome}" não foi encontrado!')
        
def visualizar_contatos():
    for i, nome in enumerate(lista_contatos):
        print(f'{i + 1}. {nome}')
        
print('\n----Bem vindo a lista de contatos----')


while True:
    print('\n----Funções----')
    print('1. adicionar contatos')
    print('2. remover contatos')
    print('3. modificar contatos')
    print('4. visualizar contatos')
    print('5. sair')
    
    escolha = int(input('\no que voçe deseja realizar?'))
    
    if escolha == 1:
        print('\n----ADICIONAR CONTATOS----')
        
        nome_contato = (input('Qual o nome do novo contato?')).strip()
        apelido = (input('Qual o apelido do novo contato?')).strip()
        numero = (input('Qual o numero do novo contato?')).strip()
        email = (input('Qual o email do novo contato?')).strip()
        
        adicionar_contatos(nome_contato, apelido, numero, email)
    
    elif escolha == 2:
        print('\n----REMOVER CONTATOS----')
        
        remover = input('Qual o nome do contato que deseja remover?').strip()
         
        remover_contato(remover)
        
    elif escolha == 3:
        contato_modificar = (input('Qual o nome do contato que deseja modificar?'))
        
        if contato_modificar in lista_contatos:
            print('\n----MODIFICAR CONTATOS----')
            
            modificar_contato(contato_modificar)
        
        else:
            print('esse contato nao foi encontrado na lista!')
        
    elif escolha == 4:
        print('\n----VISUALIZAR CONTATOS----')
        visualizar_contatos()
        
    elif escolha == 5:
        print('encerrando o sistema, ATÉ LOGO!')
        break
    
    else:
        print('por favor use os numeros de 1 a 5!')