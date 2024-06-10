Sure, here is a design for a Flask application that displays recent news articles:

## HTML Files

### index.html
- This file will be the homepage of the application, and it will display a list of recent news articles.
- It will include an HTML template with a placeholder for the list of articles.

### article.html
- This file will be used to display the details of a specific news article.
- It will include an HTML template with placeholders for the article's title, body, and author.

## Routes

### /
- This route will handle requests for the homepage.
- It will retrieve a list of recent news articles from a news API and render the `index.html` template with the list of articles.

### /article/<article_id>
- This route will handle requests for a specific news article.
- It will retrieve the article details from the news API and render the `article.html` template with the article details.

## Implementation

The following code shows how to implement the routes in Python Flask:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    articles = get_recent_news_articles()
    return render_template('index.html', articles=articles)

@app.route('/article/<article_id>')
def article(article_id):
    article = get_news_article(article_id)
    return render_template('article.html', article=article)

if __name__ == '__main__':
    app.run()
```

## Conclusion

This design provides a simple and effective way to build a Flask application that displays recent news articles. The application is easy to extend and can be customized to meet the specific needs of your project.