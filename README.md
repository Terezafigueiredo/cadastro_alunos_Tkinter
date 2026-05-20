# 📚 Cadastro de Alunos com Tkinter e SQLite

Este projeto foi desenvolvido para praticar Python com interface gráfica usando **Tkinter** e banco de dados **SQLite**.  
A ideia é ter um sistema simples de cadastro de alunos, onde é possível inserir nome e idade e visualizar todos os registros em uma tabela interativa.

---

## 🚀 Funcionalidades
- [Cadastrar alunos](ca://s?q=Funcionalidade_cadastrar_alunos) com nome e idade  
- [Visualizar registros](ca://s?q=Funcionalidade_visualizar_registros) em uma tabela organizada  
- [Barra de rolagem](ca://s?q=Funcionalidade_barra_de_rolagem) para navegar por todos os alunos  
- [Linhas alternadas](ca://s?q=Funcionalidade_linhas_alternadas) em cores para facilitar a leitura  
- [Ordenação de colunas](ca://s?q=Funcionalidade_ordenar_colunas) ao clicar no cabeçalho da tabela  

---

## 🛠️ Tecnologias utilizadas
- [Python 3](ca://s?q=Python_3)  
- [Tkinter](ca://s?q=Tkinter_interface_gráfica) (interface gráfica)  
- [SQLite](ca://s?q=SQLite_banco_de_dados) (armazenamento dos dados)  

---

## 📂 Estrutura do projeto
O código foi reorganizado para melhorar a **manutenção** e a **clareza**:
cadastro_alunos_Tkinter/
│
├── banco.py        # Conexão e criação da tabela no SQLite
├── funcoes.py      # Funções de lógica (salvar, listar, ordenar)
├── tela.py         # Interface gráfica Tkinter
└── main.py         # Ponto de entrada do programa

---

## 🔄 Alterações realizadas
- **Separação em módulos**: antes todo o código estava em um único arquivo (`main2.py`).  
  Agora cada responsabilidade está em um arquivo específico (`banco.py`, `funcoes.py`, `tela.py`).  
- **Criação do `main.py`**: centraliza a execução do projeto, deixando claro qual arquivo deve ser rodado.  
- **Uso de `.gitignore`**: configurado para ignorar arquivos temporários (`__pycache__`) e o banco local (`alunos.db`), mantendo o repositório mais limpo.  

Essas mudanças foram feitas para:
- Facilitar a leitura e manutenção do código  
- Permitir futuras expansões sem confusão  
- Deixar o repositório mais profissional e organizado  

---

## ▶️ Como executar
1. Clone o repositório:
   ```bash
   git clone https://github.com/Terezafigueiredo/cadastro_alunos_Tkinter.git
