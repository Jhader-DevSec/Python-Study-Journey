# 🏛️ Programação Orientada a Objetos (POO)

Este diretório contém a transição da programação estruturada para a Orientada a Objetos, focando na criação de classes, métodos e gestão de estados.

## 🍫 Projetos

### 1. Brownie Shop Manager
**Arquivo:** [`brownie_shop_system.py`](./brownie_shop_system.py)

Um simulador de ponto de venda (PDV) para uma loja de brownies, utilizando conceitos básicos de POO.

#### 🧠 Destaques Técnicos:
* **Encapsulamento de Atributos:** Uso do método construtor `__init__` para inicializar o estado da loja (estoque e caixa).
* **Lógica de Métodos:** Implementação de funções internas à classe (`vender` e `mostrar_relatorio`) para manipular os dados internos de forma segura.
* **Validação de Negócio:** Verificação de estoque antes de confirmar a transição financeira.
* **Tratamento de Erros:** Blocos `try/except` para garantir que o sistema de vendas não feche por erros de digitação do usuário.

### 2. Banking System Simulator
**Arquivo:** [`banking_system.py`](./banking_system.py)

Um simulador de banco que permite a criação de múltiplos usuários, cada um com sua própria instância de conta, saldo independente e registro de histórico.

#### 🧠 Destaques Técnicos:
* **Instanciação Dinâmica:** Criação de novos objetos da classe `BankAccount` em tempo de execução e armazenamento em um dicionário global.
* **Gestão de Atributos Complexos:** Uso de listas internas (`self.historical`) para rastrear todas as movimentações financeiras de cada objeto individualmente.
* **Lógica de Verificação:** Implementação de regras de negócio para impedir saques maiores que o saldo disponível.
