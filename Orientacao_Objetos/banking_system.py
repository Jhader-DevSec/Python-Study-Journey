class BankAccount():
    def __init__(self, owner):
        self.name = owner
        self.balance = 0
        self.historical = []
        
    def owner_deposit(self, value):
        self.balance += value
        self.historical.append(f"Depósito: +{value}")
        print("Valor adicionado com sucesso!")
        
    def owner_withdraw(self, value):
        if value <= self.balance:
            self.balance -= value
            self.historical.append(f"Saque: -{value}")
            print("Valor sacado com sucesso!")
        else:
            print(f"Saldo insuficiente. Saldo atual: {self.balance}")
            
    def display_extract(self):
        print(f"\nUsuário: {self.name} | Saldo Atual: {self.balance}")
        print("--- Histórico de Transações ---")
        if not self.historical:
            print("Nenhuma transação realizada.")
        for t in self.historical:
            print(t)
            
    def transfer(self, destination_accont, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.historical.append(f"transferencia enviada: -{amount} para {destination_accont.name}")
            destination_accont.owner_deposit(amount)
            destination_accont.historical.append(f"Tranferencia recebida: +{amount} de {self.name}")
        else:
            print(f"saldo insuficiente para a transferir. seu saldo atual é de: {self.balance}")

accounts_db = {}

while True:
    print("\n------------- BEM-VINDO -------------")
    print("0. valor total no banco | 1. Criar Usuário | 2. Ver Extrato | 3. Depositar | 4. Sacar | | 5. Transferir | 6. listar clientes | 7. Sair")
    

    choice = input("\nEscolha uma opção: ")
    
    if choice == "0":
        soma = 0
        for u in accounts_db.values():
            soma += u.balance
            
        print("\n----------------BANK-------------------")
        print(f"O valor total no banco é de: {soma}")
            
    elif choice == "1":
        person = input("Qual o nome do novo usuário? ").upper()
        
        if person in accounts_db:
            print("Erro: Este usuário já possui uma conta!")
        else:
            new_account = BankAccount(person)
            accounts_db[person] = new_account
            print(f"Usuário {person} adicionado com sucesso!")
            
    elif choice == "2":
        search = input("Digite o nome do usuário para ver o extrato: ").upper()
        
        if search in accounts_db:
            accounts_db[search].display_extract()
        else:
            print("Usuário não encontrado!")

    elif choice == "3":
        search = input("Para quem é o depósito? ").upper()
        
        if search in accounts_db:
            amount = float(input("Qual o valor do depósito? "))
            accounts_db[search].owner_deposit(amount)
        else:
            print("Usuário não encontrado!")

    elif choice == "4":
        search = input("De quem é o saque? ").upper()
        
        if search in accounts_db:
            amount = float(input("Qual o valor do saque? "))
            accounts_db[search].owner_withdraw(amount)
        else:
            print("Usuário não encontrado!")
            
    elif choice == "5":
        search = input("Quem vai enviar? ").upper()
        search2 = input("Quem vai receber? ").upper()
        
        if search in accounts_db and search2 in accounts_db:
            try:
                value = float(input("qual o valor da transferencia?"))
                sender = accounts_db[search]
                reciver = accounts_db[search2]
                
                sender.transfer(reciver, value)
            
            except ValueError:
                print("digite o valor em numeros apenas.")
        else:
            print("Um ou ambos os nomes nao foram encontrados no banco de dados.")
        
    elif choice == "6":
        try:
            for p in enumerate(accounts_db):
                print(p)
        except:
            print("Não temos clientes no momento!")
            
    elif choice == "7":
        print("Saindo do sistema... Até logo!")
        break