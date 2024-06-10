
from flask import Flask, render_template

app = Flask(__name__)

articles = [
    {
        "id": 1,
        "title": "First Article",
        "body": "This is the first article.",
        "author": "John Doe",
    },
    {
        "id": 2,
        "title": "Second Article",
        "body": "This is the second article.",
        "author": "Jane Doe",
    },
]

@app.route('/')
def index():
    return render_template('index.html', articles=articles)

@app.route('/article/<article_id>')
def article(article_id):
    article = next((article for article in articles if article['id'] == int(article_id)), None)
    return render_template('article.html', article=article)

if __name__ == '__main__':
    app.run()
