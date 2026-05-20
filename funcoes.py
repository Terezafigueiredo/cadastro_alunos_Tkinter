from tkinter import messagebox
import banco  # importa conexao e cursor

def listar_alunos(tabela):
    for item in tabela.get_children():
        tabela.delete(item)

    banco.cursor.execute("SELECT nome, idade FROM alunos")
    alunos = banco.cursor.fetchall()

    for i, aluno in enumerate(alunos):
        tag = "oddrow" if i % 2 == 0 else "evenrow"
        tabela.insert("", "end", values=aluno, tags=(tag,))

def salvar_aluno(entrada_nome, entrada_idade, tabela):
    nome = entrada_nome.get()
    idade = entrada_idade.get()

    if nome == "" or idade == "":
        messagebox.showerror("Erro", "Preencha todos os campos!")
        return

    banco.cursor.execute("INSERT INTO alunos (nome, idade) VALUES (?, ?)", (nome, idade))
    banco.conexao.commit()
    messagebox.showinfo("Sucesso", "Aluno cadastrado!")

    entrada_nome.delete(0, "end")
    entrada_idade.delete(0, "end")

    listar_alunos(tabela)

def ordenar(tabela, coluna, reverse=False):
    dados = [(tabela.set(k, coluna), k) for k in tabela.get_children("")]
    dados.sort(reverse=reverse)

    for index, (val, k) in enumerate(dados):
        tabela.move(k, "", index)

    tabela.heading(coluna, command=lambda: ordenar(tabela, coluna, not reverse))
