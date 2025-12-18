# NgolaTube



NgolaTube é uma Webapp p'ra visualizar uma lista de vídeos incorporados do YouTube... 

## Funcionalidades

- **Exibição de Vídeos**: Lista vídeos com título, descrição, categoria e autor.
- **Busca**: Filtre vídeos por título em tempo real.
- **Paginação**: Navegue por páginas de vídeos (6 por página).
- **Responsividade**: Interface adaptável para mobile e desktop.
- **Ícones Font Awesome**: Elementos visuais modernos.

## Tecnologias Utilizadas

- **Backend**: Flask, SQLAlchemy
- **Frontend**: HTML5, CSS3, Jinja2 templates
- **Outros**: Font Awesome para ícones, Gunicorn para produção

## Instalação

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/bybenb/NgolaTube.git
   cd ngolatube
   ```

2. **Crie um ambiente virtual** (opcional, mas recomendado):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # No Windows: .venv\Scripts\activate
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requeriments.txt
   ```

4. **Configure o banco de dados**:
   ```bash
   python criar_banco.py
   ```

## Uso

1. **Execute a aplicação**:
   ```bash
   python app.py
   ```

2. **Acesse no navegador**:
   - URL: `http://127.0.0.1:5000`
   - Navegue pelos vídeos, use a busca no cabeçalho, e pagine os resultados.

## Estrutura do Projeto

```
ngolatube/
├── app.py                 
├── criar_banco.py         
├── verificar_banco.py     
├── requeriments.txt       
├── Procfile               
├── static/
│   └── estilos.css        
├── templates/
│   └── index.html         
└── README.md              
```

## Autor

- [Beny Reis](https://facebook.com/bkapa8)
+ Contato: itsbenyreis@gmail.com
