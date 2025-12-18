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
                'titulo': 'YOUR WAY\'S BETTER (Official Lyric Video)',
                'url': 'https://www.youtube.com/embed/T1LRsp8qBY0',
                'descricao': 'OH LORD I NEED YOU NOW MORE THAN EVER!',
                'categoria': 'Musica',
                'autor': 'Forrest Frank'
            },
            {
                'titulo': 'Quantas pessoas a energia nuclear matou? Número de mortes por causa nuclear',
                'url': 'https://www.youtube.com/embed/EQcDgwhQRig',
                'descricao': 'Saiba a cada dia algo sobre o Palneta Azul.',
                'categoria': 'Entretenimento',
                'autor': 'Em Poucas Palavras - Kurzgesagt'
            },
            {
                'titulo': 'How to Make Perfect Poached Eggs - 3 Ways',
                'url': 'https://www.youtube.com/embed/pAWduxoCgVk',
                'descricao': 'Aprenda a fazer Ovos Pochê.',
                'categoria': 'Culinária',
                'autor': 'Jamie Oliver'
            },
            {
                'titulo': 'PROVANDO COMIDAS DA ANGOLA',
                'url': 'https://www.youtube.com/embed/rN_ig2aGvoY',
                'descricao': 'Exploração da comida  Angolana.',
                'categoria': 'Cultura',
                'autor': 'AchismosTV'
            },
            {
                'titulo': 'Dívidas para construir riqueza intergeracional',
                'url': 'https://www.youtube.com/embed/16AJaAPRjlc',
                'descricao': 'Introdução ao mercado de ações e investimentos.',
                'categoria': 'Finanças',
                'autor': 'Warren Buffett Academy'
            },
            {
                'titulo': 'Watch Blue Lock Episode 1 | Official Portuguese Dub',
                'url': 'https://www.youtube.com/embed/nDgB6ln16Ko&t=720s',
                'descricao': 'Conheça um dos +filosofais Animes da atualidade.',
                'categoria': 'Entretenimento',
                'autor': 'Crunchyroll Brasil'
            },          
            {
                'titulo': 'Até o Diabo tinha medo da minha Mãe | Stand-Up Comedy',
                'url': 'https://www.youtube.com/embed/Ey8MPsQxxX4',
                'descricao': 'Show de comédia stand-up com artistas locais.',
                'categoria': 'Comédia',
                'autor': 'Sou Daniel Lopes'
            },
            {
                'titulo': 'It Smelled of Death... (Full Episode) | Something Bit Me',
                'url': 'https://www.youtube.com/embed/vH98XFxys8M',
                'descricao': 'Explora as histórias reais e peculiares de picadas de insetos, ferroadas e ataques de animais que levaram pessoas ao pronto-socorro por causa de veneno, doenças ou pela força bruta de suas mandíbulas.',
                'categoria': 'Documentário',
                'autor': 'National Geographic'
            },
            {
                'titulo': 'Como Criar um Canal no YouTube | Guia Completo',
                'url': 'https://www.youtube.com/embed/05FIltf3yqk',
                'descricao': 'Passos para iniciar um canal de sucesso.',
                'categoria': 'YouTube',
                'autor': 'JOBA'
            },
            {
                'titulo': 'Como lidar com autocrítica: 6 perguntas para te ajudar',
                'url': 'https://www.youtube.com/embed/gSeBOGf3Cf4',
                'descricao': 'Dicas para manter a saúde mental em dia.',
                'categoria': 'Saúde',
                'autor': 'Universo Psicologia'
            }
        ]
        
        for data in videos_data:
            video = Video(**data)
            db.session.add(video)
        
        db.session.commit()

print("Banco de dados criado com sucesso!")
