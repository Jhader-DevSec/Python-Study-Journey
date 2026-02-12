class BrownieShop:
    def __init__(self, estoque_inicial, preco):
        self.estoque = estoque_inicial
        self.preco = preco
        self.caixa = 0

    def vender(self, quantidade):
        if self.estoque >= quantidade:
            self.estoque -= quantidade
            self.caixa += quantidade * self.preco
            print('venda realizada!')
            
        else:
            print('estoque insuficiente!')

        pass

    def mostrar_relatorio(self):
        print(f"Estoque atual: {self.estoque}")
        print(f"Total em caixa: R${self.caixa}")


minha_loja = BrownieShop(20, 5.0)

while True:
    print("--------painel de vendas-------")
    print("1. vender | 2. sair")
    
    try:
      user =  int(input('escolha:'))
        
    except:
        print("ultilize apenas números por favor!")
        continue
    if user == 2:
        break
    
    elif user == 1:
        try:
            qtd= input("quantos brownies deseja vender?")
            qtd_convertida = int(qtd)
            minha_loja.vender(qtd_convertida)
            
            minha_loja.mostrar_relatorio()

        except:
            print("por favor digite em numeros a quantidade desejada!")
            
        minha_loja.mostrar_relatorio()
        
    else:
        print("apenas ultilize os numeros 1 e 2!")