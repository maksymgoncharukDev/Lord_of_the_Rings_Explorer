from flask import Flask, render_template
import requests

app = Flask(__name__)

API_KEY = 'FeAMtkniob2WQ3ZXRyPz'
BASE_URL = 'https://the-one-api.dev/v2'
HEADERS = {'Authorization': f'Bearer {API_KEY}'}

@app.route('/')
def index():
    response = requests.get(f'{BASE_URL}/character?limit=10', headers=HEADERS)
    data = response.json()
    characters = data.get('docs', [])
    return render_template('index.html', characters=characters)

@app.route('/quotes')
def quotes():
    response = requests.get(f'{BASE_URL}/quote?limit=5', headers=HEADERS)
    data = response.json()
    quotes = data.get('docs', [])
    return render_template('quotes.html', quotes=quotes)

@app.route('/movies')
def movies():
    response = requests.get(f'{BASE_URL}/movie', headers=HEADERS)
    data = response.json()
    movies = data.get('docs', [])
    return render_template('movies.html', movies=movies)

if __name__ == '__main__':
    app.run(debug=True)
