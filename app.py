from flask import Flask, render_template
import os

app = Flask(__name__)

posts = [
    {
        'autor': 'Cleo Will',
        'title': 'Resolução da EDO com série de potências,
        'date_post': '2025-03-05',
        'image': 'cal.jpg',
        'sinopse': 'Neste post, abordamos a resolução de uma Equação Diferencial Ordinária (EDO) utilizando o método das séries de potências, uma técnica fundamental na análise de soluções aproximadas para equações complexas.',
        'content_file': 'edopotseries.txt',
        'tag': ['Equações diferenciais'],
        'font':' Boyce, W. E., & DiPrima, R. C. (2017). Equações Diferenciais Elementares (10ª ed.). Wiley.'
    },
   
]

images = ['car1.jpg', 'car2.jpg', 'car3.jpg']

def load_post_content(filename):
    try:
        file_path = os.path.join('static', 'posts', filename)
        print(f"Tentando carregar o arquivo: {file_path}")
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado - {file_path}")
        return "Conteúdo não encontrado."
    except Exception as e:
        print(f"Erro inesperado: {e}")  
        return "Erro inesperado ao carregar o conteúdo."

@app.route('/')
def home():
    
    sorted_posts = sorted(posts, key=lambda p: p['date_post'], reverse=True)
    recent_posts = sorted_posts[:5]  
    return render_template('index.html', posts=sorted_posts, recent_posts=recent_posts, images=images)

@app.route('/post/<string:title>')
def post(title):
    post = next((p for p in posts if p['title'] == title), None)
    if post:
        post_content = load_post_content(post['content_file'])
        post['content'] = post_content
    
    recent_posts = sorted(posts, key=lambda p: p['date_post'], reverse=True)[:5]
    return render_template('post.html', post=post, recent_posts=recent_posts)

@app.route('/category/<string:title>')
def category(title):
    
    filtered_posts = [p for p in posts if title in p['tag']]
    sorted_filtered_posts = sorted(filtered_posts, key=lambda p: p['date_post'], reverse=True)
    return render_template('category.html', posts=sorted_filtered_posts, tag=title)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.getenv("PORT", 5000)))

