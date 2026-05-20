import tkinter as tk
from tkinter import ttk
import funcoes

# Criar janela
janela = tk.Tk()
janela.title("Cadastro de alunos")
janela.geometry("500x400")

# Labels
tk.Label(janela, text="Nome").grid(row=0, column=0, padx=10, pady=10)
tk.Label(janela, text="Idade").grid(row=1, column=0, padx=10, pady=10)

# Entradas
entrada_nome = tk.Entry(janela)
entrada_nome.grid(row=0, column=1)

entrada_idade = tk.Entry(janela)
entrada_idade.grid(row=1, column=1)

# Botão salvar
botao_salvar = tk.Button(janela, text="Salvar",
                         command=lambda: funcoes.salvar_aluno(entrada_nome, entrada_idade, tabela))
botao_salvar.grid(row=2, column=1, pady=10)

# Configurar expansão
janela.grid_rowconfigure(3, weight=1)
janela.grid_columnconfigure(0, weight=1)

# Tabela
tabela = ttk.Treeview(janela, columns=("nome", "idade"), show="headings")
tabela.heading("nome", text="Nome", command=lambda: funcoes.ordenar(tabela, "nome"))
tabela.heading("idade", text="Idade", command=lambda: funcoes.ordenar(tabela, "idade"))

tabela.column("nome", width=250)
tabela.column("idade", width=100)

tabela.grid(row=3, column=0, columnspan=2, sticky="nsew")

# Scrollbar
scrollbar = tk.Scrollbar(janela, orient="vertical", command=tabela.yview)
tabela.configure(yscrollcommand=scrollbar.set)
scrollbar.grid(row=3, column=2, sticky="ns")

# Estilo da tabela
style = ttk.Style()
style.configure("Treeview", font=("Arial", 11), rowheight=25)
style.configure("Treeview.Heading", font=("Arial", 12, "bold"))

tabela.tag_configure("oddrow", background="#f0f0f0")
tabela.tag_configure("evenrow", background="#ffffff")

# Carregar dados
funcoes.listar_alunos(tabela)

janela.mainloop()
