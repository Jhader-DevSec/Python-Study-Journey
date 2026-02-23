# 🏛️ Programação Orientada a Objetos (POO)

Este diretório contém a transição da programação estruturada para a Orientada a Objetos, focando na criação de classes, métodos e gestão de estados.

## 🍫 Projetos

### 1. Brownie Shop Manager
**Arquivo:** [`brownie_shop_system.py`](./brownie_shop_system.py)

Um simulador de ponto de venda (PDV) para uma loja de brownies, utilizando conceitos básicos de POO.

#### 🧠 Destaques Técnicos:
* **Encapsulamento de Atributos:** Uso do método construtor `__init__` para inicializar o estado da loja (estoque e caixa).
* **Lógica de Métodos:** Implementação de funções internas à classe para manipular os dados internos de forma segura.
* **Validação de Negócio:** Verificação de estoque antes de confirmar a transição financeira.
* **Tratamento de Erros:** Blocos `try/except` para garantir que o sistema de vendas não feche por erros de digitação.

---

### 2. Banking System Simulator (v3.0 - Security Update) 🛡️
**Arquivo:** [`banking_system.py`](./banking_system.py)

Um simulador bancário profissional que integra lógica de segurança cibernética à Orientação a Objetos, permitindo autenticação por senha e rastreabilidade total de operações.

#### 🧠 Destaques Técnicos da Atualização:
* **Integração de Segurança (DevSec):** Implementação de um gerador de senhas de alta entropia para novos usuários e validação de credenciais em métodos sensíveis (Saque, Extrato e Transferência).
* **Rastreabilidade (Logging):** Uso de listas internas (`historical`) para registrar cada movimentação financeira, garantindo integridade e histórico para o usuário.
* **Encapsulamento de Validação:** Criação do método `check_password()` para centralizar a lógica de segurança, evitando repetição de código e seguindo o princípio DRY (Don't Repeat Yourself).
* **Gestão Dinâmica de Objetos:** Uso de dicionários globais para simular um banco de dados em memória, permitindo operações complexas entre diferentes instâncias de contas.
