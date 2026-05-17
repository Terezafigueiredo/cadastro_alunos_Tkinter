import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3

# Conecta banco
conexao = sqlite3.connect('alunos.db')
cursor = conexao.cursor()

# Cria tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    idade INTEGER
)
""")

# Função para listar alunos
def listar_alunos():
    for item in tabela.get_children():
        tabela.delete(item)

    cursor.execute("SELECT nome, idade FROM alunos")
    alunos = cursor.fetchall()

    for i, aluno in enumerate(alunos):
        tag = "oddrow" if i % 2 == 0 else "evenrow"
        tabela.insert("", tk.END, values=aluno, tags=(tag,))

# Função para salvar aluno
def salvar_aluno():
    nome = entrada_nome.get()
    idade = entrada_idade.get()

    if nome == "" or idade == "":
        messagebox.showerror("Erro", "Preencha todos os campos!")
        return

    cursor.execute("INSERT INTO alunos (nome, idade) VALUES (?, ?)", (nome, idade))
    conexao.commit()
    messagebox.showinfo("Sucesso", "Aluno cadastrado!")

    entrada_nome.delete(0, tk.END)
    entrada_idade.delete(0, tk.END)

    listar_alunos()

# Função para ordenar colunas
def ordenar(coluna, reverse=False):
    dados = [(tabela.set(k, coluna), k) for k in tabela.get_children("")]
    dados.sort(reverse=reverse)

    for index, (val, k) in enumerate(dados):
        tabela.move(k, "", index)

    tabela.heading(coluna, command=lambda: ordenar(coluna, not reverse))

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
botao_salvar = tk.Button(janela, text="Salvar", command=salvar_aluno)
botao_salvar.grid(row=2, column=1, pady=10)

# Configurar expansão
janela.grid_rowconfigure(3, weight=1)
janela.grid_columnconfigure(0, weight=1)

# Tabela
tabela = ttk.Treeview(janela, columns=("nome", "idade"), show="headings")
tabela.heading("nome", text="Nome", command=lambda: ordenar("nome"))
tabela.heading("idade", text="Idade", command=lambda: ordenar("idade"))

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

listar_alunos()
janela.mainloop()
