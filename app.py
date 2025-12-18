from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

VIDEOS_PER_PAGE = 6

@app.route('/')
def pagina_principal():
    page = request.args.get('page', 1, type=int)
    offset = (page - 1) * VIDEOS_PER_PAGE
    
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()
    
    # Contar total de vídeos
    cursor.execute("SELECT COUNT(*) FROM videos")
    total_videos = cursor.fetchone()[0]
    total_pages = (total_videos + VIDEOS_PER_PAGE - 1) // VIDEOS_PER_PAGE
    
    # Buscar vídeos com limite
    cursor.execute("SELECT titulo, url FROM videos LIMIT ? OFFSET ?", (VIDEOS_PER_PAGE, offset))
    lista_videos = cursor.fetchall()
    conexao.close()
    
    return render_template('index.html', videos=lista_videos, page=page, total_pages=total_pages)


# 2-5-14-25
if __name__ == '__main__':
    app.run(debug=True)
