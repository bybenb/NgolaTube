from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

VIDEOS_PER_PAGE = 6

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(500), nullable=False)
    descricao = db.Column(db.Text)
    categoria = db.Column(db.String(100))
    autor = db.Column(db.String(100))

@app.route('/')
def pagina_principal():
    page = request.args.get('page', 1, type=int)
    query = request.args.get('q', '').strip()
    offset = (page - 1) * VIDEOS_PER_PAGE
    
    if query:
        videos_query = Video.query.filter(Video.titulo.like(f'%{query}%'))
        total_videos = videos_query.count()
        videos = videos_query.limit(VIDEOS_PER_PAGE).offset(offset).all()
    else:
        total_videos = Video.query.count()
        videos = Video.query.limit(VIDEOS_PER_PAGE).offset(offset).all()
    
    total_pages = (total_videos + VIDEOS_PER_PAGE - 1) // VIDEOS_PER_PAGE
    
    return render_template('index.html', videos=videos, page=page, total_pages=total_pages, query=query)


# 2-5-14-25
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
