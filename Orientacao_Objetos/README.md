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

### 2. Banking System Simulator (v2.0)
**Arquivo:** [`banking_system.py`](./banking_system.py)

Um simulador bancário robusto que gerencia múltiplas contas através de instâncias de classes, permitindo interações financeiras complexas entre diferentes usuários.

#### 🧠 Destaques Técnicos da Atualização:
* **Interação entre Objetos:** Implementação de transferências diretas onde um objeto altera o estado de outro (remetente e destinatário) através de métodos internos.
* **Agregação de Dados:** Uso de loops e métodos de dicionário (`values()`) para calcular métricas globais, como o saldo total sob custódia do banco.
* **Tratamento de Erros:** Uso estratégico de blocos `try/except` para validar entradas numéricas e garantir a integridade do sistema durante transferências e saques.
* **Gestão de Banco de Dados em Memória:** Mapeamento de objetos em um dicionário global, permitindo busca, listagem e manipulação de contas por nome de usuário.
