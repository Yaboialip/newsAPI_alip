from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Ganti dengan API Key Anda
API_KEY = 'ad76b0b2f9d24682842924ff71c6b806'
BASE_URL = 'https://newsapi.org/v2/everything'

@app.route('/', methods=['GET', 'POST'])
def index():
    articles = []
    error = None
    if request.method == 'POST':
        query = request.form['query']
        params = {
            'q': query,
            'apiKey': API_KEY,
            'language': 'en',
            'pageSize': 10
        }
        response = requests.get(BASE_URL, params=params)
        print("API Response Status Code:", response.status_code)  # Debugging
        print("API Response JSON:", response.json())  # Debugging
        if response.status_code == 200:
            data = response.json()
            articles = data.get('articles', [])
            if not articles:
                error = "No articles found."
        else:
            error = f"Failed to fetch data. Error: {response.status_code}"
    return render_template('index.html', articles=articles, error=error)

if __name__ == '__main__':
    app.run(debug=True)