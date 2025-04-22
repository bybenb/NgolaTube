import sqlite3


conexao = sqlite3.connect('banco.db')


cursor = conexao.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        url TEXT NOT NULL
    )
''')





cursor.execute("INSERT INTO videos (titulo, url) VALUES ('[FREE] CBG x Wizy x Kelson Most Wanted Type Beat IMPÉRIO (Prod.Steam Blood)', 'https://www.youtube.com/embed/X-w2i0aqIzU')")


cursor.execute("INSERT INTO videos (titulo, url) VALUES ('Título do vídeo aqui', 'https://www.youtube.com/embed/U2bMv-QBGB8')")




cursor.execute("INSERT INTO videos (titulo, url) VALUES ('What really matters at the end of life | BJ Miller | TED', 'https://www.youtube.com/embed/apbSsILLh28?start=7')")

cursor.execute("INSERT INTO videos (titulo, url) VALUES ('O Lince Sabe Quem é O Pai | Shadow Fight 2', 'https://www.youtube.com/embed/yRMt8SoZkZg?start=15')")

cursor.execute("INSERT INTO videos (titulo, url) VALUES ('Ela factura milhões com o digital | Dinheiro Limpo Podcast Ep.36', 'https://www.youtube.com/embed/b6nP_Ak4A6k')")



conexao.commit()
conexao.close()

print("Banco de dados criado com sucesso!")
# 2-5-14-25
