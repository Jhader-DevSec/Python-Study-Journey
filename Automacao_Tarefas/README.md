# ⚙️ Automação de Tarefas e Manipulação de Arquivos

Este diretório contém scripts desenvolvidos para automatizar rotinas do sistema operacional e manipular arquivos externos.

## 📄 Projetos

### 1. PDF & DOCX Modifier Toolkit
**Arquivos:** [`pdf_modifier.py`](./pdf_modifier.py) | [`requirements.txt`](./requirements.txt)

Uma ferramenta de Linha de Comando (CLI) para conversão, leitura e modificação de documentos.

#### 🧠 Destaques Técnicos:
* **Bibliotecas Externas:** Integração de pacotes via `pip` (`pdf2docx`, `pypdf`, `python-docx`).
* **Manipulação de Caminhos:** Uso da biblioteca nativa `pathlib` para extrair sufixos e nomes lógicos dos arquivos independentemente do sistema operacional.
* **Tratamento de Exceções I/O:** Captura de `FileNotFoundError` para evitar quebra de sistema caso o usuário digite um caminho incorreto.
* **Conversão e Escrita:** Algoritmo que lê propriedades de parágrafos do Word e injeta novos textos diretamente no arquivo.

## 🛠 Como instalar as dependências
Antes de rodar o script, instale os pacotes necessários utilizando o arquivo requirements:
```bash
pip install -r requirements.txt
