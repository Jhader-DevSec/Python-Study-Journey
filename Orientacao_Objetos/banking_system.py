import random
import string

class BankAccount():
    def __init__(self, owner, password):
        self.name = owner
        self.balance = 0
        self.historical = []
        self.password = password  
        
    def check_password(self):
        attempt = input(f"Digite a senha para a conta de {self.name}: ")
        if attempt == self.password:
            return True
        print("Senha incorreta! Operação cancelada.")
        return False

    def owner_deposit(self, value):
        self.balance += value
        self.historical.append(f"Depósito: +{value}")
        print("Valor adicionado com sucesso!")
        
    def owner_withdraw(self, value):
        if self.check_password(): 
            if value <= self.balance:
                self.balance -= value
                self.historical.append(f"Saque: -{value}")
                print("Valor sacado com sucesso!")
            else:
                print(f"Saldo insuficiente. Saldo atual: {self.balance}")
            
    def display_extract(self):
        if self.check_password(): 
            print(f"\nUsuário: {self.name} | Saldo Atual: {self.balance}")
            print("--- Histórico de Transações ---")
            if not self.historical:
                print("Nenhuma transação realizada.")
            for t in self.historical:
                print(t)
            
    def transfer(self, destination_account, amount):
        if self.check_password(): 
            if amount <= self.balance:
                self.balance -= amount
                self.historical.append(f"transferencia enviada: -{amount} para {destination_account.name}")
                destination_account.balance += amount 
                destination_account.historical.append(f"Tranferencia recebida: +{amount} de {self.name}")
                print("Transferência concluída com sucesso!")
            else:
                print(f"saldo insuficiente para a transferir.")

def gerar_senha_automatica(comprimento=8):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for i in range(comprimento))

accounts_db = {}

while True:
    print("\n------------- BEM-VINDO -------------")
    print("1. Criar Usuário | 2. Ver Extrato | 3. Depositar | 4. Sacar | 5. Transferir | 6. Sair")
    
    choice = input("\nEscolha uma opção: ")
            
    if choice == "1":
        person = input("Qual o nome do novo usuário? ").upper()
        if person in accounts_db:
            print("Erro: Este usuário já possui uma conta!")
        else:
            tipo_senha = input("Deseja (1) Criar senha ou (2) Gerar senha forte automática? ")
            if tipo_senha == "2":
                senha = gerar_senha_automatica()
                print(f"Senha gerada para {person}: {senha} (Guarde-a bem!)")
            else:
                senha = input("Defina sua senha: ")
            
            new_account = BankAccount(person, senha)
            accounts_db[person] = new_account
            print(f"Usuário {person} adicionado com sucesso!")
            
    elif choice == "2":
        search = input("Nome do usuário: ").upper()
        if search in accounts_db:
            accounts_db[search].display_extract()
        else:
            print("Usuário não encontrado!")

    elif choice == "3":
        search = input("Para quem é o depósito? ").upper()
        if search in accounts_db:
            amount = float(input("Valor: "))
            accounts_db[search].owner_deposit(amount)
        else:
            print("Usuário não encontrado!")

    elif choice == "4":
        search = input("De quem é o saque? ").upper()
        if search in accounts_db:
            amount = float(input("Valor: "))
            accounts_db[search].owner_withdraw(amount)

    elif choice == "5":
        search = input("Quem vai enviar? ").upper()
        search2 = input("Quem vai receber? ").upper()
        
        if search in accounts_db and search2 in accounts_db:
            try:
                value = float(input("Qual o valor? "))
                accounts_db[search].transfer(accounts_db[search2], value)
            except ValueError:
                print("Digite apenas números.")
        else:
            print("Conta não encontrada.")
            
    elif choice == "6":

        break
