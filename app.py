from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

VIDEOS_PER_PAGE = 6

@app.route('/')
def pagina_principal():
    page = request.args.get('page', 1, type=int)
    query = request.args.get('q', '').strip()
    offset = (page - 1) * VIDEOS_PER_PAGE
    
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()
    
    if query:
        # Contar vídeos filtrados
        cursor.execute("SELECT COUNT(*) FROM videos WHERE titulo LIKE ?", ('%' + query + '%',))
        total_videos = cursor.fetchone()[0]
        # Buscar vídeos filtrados
        cursor.execute("SELECT titulo, url, descricao, categoria, autor FROM videos WHERE titulo LIKE ? LIMIT ? OFFSET ?", ('%' + query + '%', VIDEOS_PER_PAGE, offset))
    else:
        # Contar todos
        cursor.execute("SELECT COUNT(*) FROM videos")
        total_videos = cursor.fetchone()[0]
        # Buscar todos
        cursor.execute("SELECT titulo, url, descricao, categoria, autor FROM videos LIMIT ? OFFSET ?", (VIDEOS_PER_PAGE, offset))
    
    total_pages = (total_videos + VIDEOS_PER_PAGE - 1) // VIDEOS_PER_PAGE
    lista_videos = cursor.fetchall()
    conexao.close()
    
    return render_template('index.html', videos=lista_videos, page=page, total_pages=total_pages, query=query)


# 2-5-14-25
if __name__ == '__main__':
    app.run(debug=True)
