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
            },
            {
                'titulo': 'Como Fazer um Site Profissional | HTML, CSS e JavaScript',
                'url': 'https://www.youtube.com/embed/Ejkb_YpuHWs',
                'descricao': 'Tutorial completo para criar sites responsivos.',
                'categoria': 'Educação',
                'autor': 'Curso em Vídeo'
            },
            {
                'titulo': 'Top 10 Jogos de 2023 | Análise Completa',
                'url': 'https://www.youtube.com/embed/8aGhZQkoFbQ',
                'descricao': 'Revisão dos melhores jogos lançados no ano.',
                'categoria': 'Entretenimento',
                'autor': 'IGN'
            },
            {
                'titulo': 'Receita de Feijoada Completa | Passo a Passo',
                'url': 'https://www.youtube.com/embed/4Jv9xZ9w9zA',
                'descricao': 'Aprenda a fazer a tradicional feijoada brasileira.',
                'categoria': 'Culinária',
                'autor': 'Panelinha'
            },
            {
                'titulo': 'História da Música Angolana | Documentário',
                'url': 'https://www.youtube.com/embed/5xZvK9z9z9z',
                'descricao': 'Exploração da evolução da música em Angola.',
                'categoria': 'Documentário',
                'autor': 'TPA'
            },
            {
                'titulo': 'Como Investir em Ações | Guia para Iniciantes',
                'url': 'https://www.youtube.com/embed/6yZwK9z9z9z',
                'descricao': 'Introdução ao mercado de ações e investimentos.',
                'categoria': 'Finanças',
                'autor': 'Warren Buffett Academy'
            },
            {
                'titulo': 'Viagem a Luanda | Turismo em Angola',
                'url': 'https://www.youtube.com/embed/7zZwK9z9z9z',
                'descricao': 'Descubra os pontos turísticos de Luanda.',
                'categoria': 'Turismo',
                'autor': 'Visit Angola'
            },
            {
                'titulo': 'Kizomba Moderna | Aula de Dança',
                'url': 'https://www.youtube.com/embed/8aZwK9z9z9z',
                'descricao': 'Aprenda passos básicos de kizomba.',
                'categoria': 'Dança',
                'autor': 'Kizomba School'
            },
            {
                'titulo': 'Inteligência Artificial no Futuro | Palestra',
                'url': 'https://www.youtube.com/embed/9bZwK9z9z9z',
                'descricao': 'Discussão sobre o impacto da IA na sociedade.',
                'categoria': 'Tecnologia',
                'autor': 'MIT Technology Review'
            },
            {
                'titulo': 'Stand-Up Comedy | Humor Angolano',
                'url': 'https://www.youtube.com/embed/0cZwK9z9z9z',
                'descricao': 'Show de comédia stand-up com artistas locais.',
                'categoria': 'Comédia',
                'autor': 'Angola Comedy'
            },
            {
                'titulo': 'Fotografia de Natureza | Dicas Profissionais',
                'url': 'https://www.youtube.com/embed/1dZwK9z9z9z',
                'descricao': 'Técnicas para fotografar paisagens naturais.',
                'categoria': 'Fotografia',
                'autor': 'National Geographic'
            },
            {
                'titulo': 'Como Criar um Canal no YouTube | Guia Completo',
                'url': 'https://www.youtube.com/embed/2eZwK9z9z9z',
                'descricao': 'Passos para iniciar um canal de sucesso.',
                'categoria': 'YouTube',
                'autor': 'PewDiePie'
            },
            {
                'titulo': 'Saúde Mental | Como Lidar com o Stress',
                'url': 'https://www.youtube.com/embed/3fZwK9z9z9z',
                'descricao': 'Dicas para manter a saúde mental em dia.',
                'categoria': 'Saúde',
                'autor': 'Psicologia Hoje'
            }
        ]
        
        for data in videos_data:
            video = Video(**data)
            db.session.add(video)
        
        db.session.commit()

print("Banco de dados criado com sucesso!")
