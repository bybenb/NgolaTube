import sqlite3


conexao = sqlite3.connect('banco.db')


cursor = conexao.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        url TEXT NOT NULL,
        descricao TEXT,
        categoria TEXT,
        autor TEXT
    )
''')

# Adicionar colunas se não existirem (para tabelas existentes)
try:
    cursor.execute("ALTER TABLE videos ADD COLUMN descricao TEXT")
except sqlite3.OperationalError:
    pass  # Coluna já existe
try:
    cursor.execute("ALTER TABLE videos ADD COLUMN categoria TEXT")
except sqlite3.OperationalError:
    pass
try:
    cursor.execute("ALTER TABLE videos ADD COLUMN autor TEXT")
except sqlite3.OperationalError:
    pass





cursor.execute("INSERT INTO videos (titulo, url, descricao, categoria, autor) VALUES ('[FREE] CBG x Wizy x Kelson Most Wanted Type Beat IMPÉRIO (Prod.Steam Blood)', 'https://www.youtube.com/embed/X-w2i0aqIzU', 'Beat instrumental angolano para rappers.', 'Música', 'Steam Blood')")


cursor.execute("INSERT INTO videos (titulo, url, descricao, categoria, autor) VALUES ('Standard Bank de Angola | Proposta de Valor Oil & Gas', 'https://www.youtube.com/embed/U2bMv-QBGB8', 'Apresentação sobre serviços bancários para o setor de petróleo e gás.', 'Negócios', 'Standard Bank Angola')")




cursor.execute("INSERT INTO videos (titulo, url, descricao, categoria, autor) VALUES ('What really matters at the end of life | BJ Miller | TED', 'https://www.youtube.com/embed/apbSsILLh28?start=7', 'Palestra sobre cuidados paliativos e significado da vida.', 'Educação', 'BJ Miller')")

cursor.execute("INSERT INTO videos (titulo, url, descricao, categoria, autor) VALUES ('O Lince Sabe Quem é O Pai | Shadow Fight 2', 'https://www.youtube.com/embed/yRMt8SoZkZg?start=15', 'Vídeo humorístico de gameplay.', 'Entretenimento', 'Desconhecido')")

cursor.execute("INSERT INTO videos (titulo, url, descricao, categoria, autor) VALUES ('Ela factura milhões com o digital | Dinheiro Limpo Podcast Ep.36', 'https://www.youtube.com/embed/b6nP_Ak4A6k', 'Episódio sobre empreendedorismo digital.', 'Podcast', 'Dinheiro Limpo')")



conexao.commit()
conexao.close()

print("Banco de dados criado com sucesso!")
# 2-5-14-25
