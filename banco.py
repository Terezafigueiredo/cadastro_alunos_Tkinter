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
conexao.commit()