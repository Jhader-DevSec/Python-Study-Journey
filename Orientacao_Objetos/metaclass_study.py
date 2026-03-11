#=========================================
# criando a metaclasse de verificação de requisitos e modificação
#=========================================
class ExploitValidator(type):
    def __new__ (cls, name, bases, dict, /, **kwds):
        print(f"\nverificando requisitos para criação da classe {name} ")
        print("--------------------------")
        
        # verifica se as condicoes predefinidas estao na classe 
        if "alvo_ip" not in dict:
            raise TypeError(f"Prjeto {name} nao definiu um 'ip_alvo'.")
        if "executar_ataque" not in dict:
            raise TypeError(f"Projeto {name} nao definiu função 'executar_ataque'.")
        
        # insere o valor autor caso a classe esteja nos parametros
        dict["autor"] = "Jhader-Devsec"
        
        return super().__new__(cls, name, bases, dict, **kwds)
    
# ==========================================
# ÁREA DE TESTES 
# ==========================================

print("Teste 1: Criando um exploit perfeito...")
class ExploitWeb(metaclass=ExploitValidator):
    alvo_ip = "10.0.0.5"
    
    def executar_ataque(self):
        print("Atacando servidor web...")

ferramenta = ExploitWeb()
print(f"O autor dessa ferramenta secreta é: {ferramenta.autor}\n")


print("Teste 2: Esquecendo a função de ataque (Isso DEVE gerar um erro vermelho e parar o código)")
#class ExploitFalho(metaclass=ExpoitValidator):
#    alvo_ip = "192.168.1.1"


print("Teste 3: Esquecendo o alvo (Isso DEVE gerar um erro vermelho e parar o código)")
#class ExploitCego(metaclass=ExploitValidator):
#    def executar_ataque(self):
#       print("Atirando no escuro...")