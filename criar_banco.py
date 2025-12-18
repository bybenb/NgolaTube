from app import db, Video, app
import sqlite3  # Para backup se necessário

with app.app_context():
    db.create_all()
    
    # Adicionar vídeos de exemplo se não existirem
    if Video.query.count() == 0:
        videos_data = [
            {
                'titulo': '[FREE] CBG x Wizy x Kelson Most Wanted Type Beat IMPÉRIO (Prod.Steam Blood)',
                'url': 'https://www.youtube.com/embed/X-w2i0aqIzU',
                'descricao': 'Beat instrumental angolano para rappers.',
                'categoria': 'Música',
                'autor': 'Steam Blood'
            },
            {
                'titulo': 'Standard Bank de Angola | Proposta de Valor Oil & Gas',
                'url': 'https://www.youtube.com/embed/U2bMv-QBGB8',
                'descricao': 'Apresentação sobre serviços bancários para o setor de petróleo e gás.',
                'categoria': 'Negócios',
                'autor': 'Standard Bank Angola'
            },
            {
                'titulo': 'What really matters at the end of life | BJ Miller | TED',
                'url': 'https://www.youtube.com/embed/apbSsILLh28?start=7',
                'descricao': 'Palestra sobre cuidados paliativos e significado da vida.',
                'categoria': 'Educação',
                'autor': 'BJ Miller'
            },
            {
                'titulo': 'O Lince Sabe Quem é O Pai | Shadow Fight 2',
                'url': 'https://www.youtube.com/embed/yRMt8SoZkZg?start=15',
                'descricao': 'Vídeo humorístico de gameplay.',
                'categoria': 'Entretenimento',
                'autor': 'BrancoPlayer'
            },
            {
                'titulo': 'Lucas A.R.T. - ASTA',
                'url': 'https://www.youtube.com/embed/-dkNV505w5A',
                'descricao': 'Maior Canal de Rap Nerd do Brasil.',
                'categoria': 'Música',
                'autor': '7Minutoz'
            },
            {
                'titulo': 'Duolingo Anime',
                'url': 'https://www.youtube.com/embed/tlotyLGia5I?start=15',
                'descricao': 'Maior escola de Idiomas Online.',
                'categoria': 'Educação',
                'autor': 'DUOLINGO'
            },
            {
                'titulo': 'Ela factura milhões com o digital | Dinheiro Limpo Podcast Ep.36',
                'url': 'https://www.youtube.com/embed/b6nP_Ak4A6k',
                'descricao': 'Episódio sobre empreendedorismo digital.',
                'categoria': 'Podcast',
                'autor': 'Dinheiro Limpo'
            }
        ]
        
        for data in videos_data:
            video = Video(**data)
            db.session.add(video)
        
        db.session.commit()

print("Banco de dados criado com sucesso!")
