from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def pagina_principal():
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT titulo, url FROM videos")
    lista_videos = cursor.fetchall()
    conexao.close()
    return render_template('index.html', videos=lista_videos)


# 2-5-14-25
if __name__ == '__main__':
    app.run(debug=True)
