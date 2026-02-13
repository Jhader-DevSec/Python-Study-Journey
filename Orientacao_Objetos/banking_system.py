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


accounts_db = {}

while True:
    print("\n------------- BEM-VINDO -------------")
    print("1. Criar Usuário | 2. Ver Extrato | 3. Depositar | 4. Sacar | 5. Sair")
    
    choice = input("Escolha uma opção: ")
    
    if choice == "1":
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
        print("Saindo do sistema... Até logo!")
        break