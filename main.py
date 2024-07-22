from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('quote.html')

@app.route('/get_quote')
def get_quote():
    try:
        response = requests.get('https://api.quotable.io/random')
        response.raise_for_status()
        quote_data = response.json()
        quote = quote_data.get('content', 'No quote found')
        author = quote_data.get('author', 'Unknown author')
    except requests.exceptions.RequestException as e:
        quote = 'Не удалось получить цитату в это время.'
        author = str(e)
    return jsonify({'quote': quote, 'author': author})

if __name__ == '__main__':
    app.run(debug=True)
