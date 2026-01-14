# 📉 Estudo de Caso: Otimização de Contagem Regressiva

Este diretório contém duas versões de um algoritmo de contagem regressiva. O objetivo foi refatorar a lógica inicial para aplicar **Boas Práticas de Programação (Clean Code)** e modularização.

## 📂 Arquivos
* [v1_inicial.py](./v1_inicial.py): Minha primeira solução lógica.
* [v2_refatorado.py](./v2_refatorado.py): Solução otimizada seguindo padrões da indústria.

---

## 💡 Por que a Versão 2 é Profissional?

Abaixo detalho as correções aplicadas na refatoração:

### 1. Escopo de Definição (Function Hoisting)
* **Antes (v1):** A função `contagem_regressiva` era definida *dentro* do bloco `if`. Isso é uma má prática, pois a função é recriada condicionalmente e fica "escondida" no meio da lógica.
* **Depois (v2):** A função é definida no **topo do arquivo** (Escopo Global). Isso segue a PEP-8 (guia de estilo Python), tornando o código previsível: primeiro definimos as *ferramentas*, depois as *usamos*.

### 2. Princípio da Responsabilidade Única
* **Antes (v1):** A lógica de validação (`if n >= 0`) e a definição da função estavam misturadas.
* **Depois (v2):** 1. A função apenas executa a ação (contar).
    2. O programa principal cuida da interação com o usuário (inputs) e validação.
    
Isso facilita a **manutenção** e permite que a função de contagem seja reutilizada em outras partes do sistema sem depender do `input` do usuário.

### 3. Prevenção de Erros (Shadowing)
Ao mover a função para fora, evitamos riscos de a função não existir caso a condição do `if` falhe, garantindo maior estabilidade ao software.

---
*Estudo realizado por [Jhader Augusto](https://github.com/Jhader-DevSec)*