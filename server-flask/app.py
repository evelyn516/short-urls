from flask import Flask, render_template, redirect, url_for, request, Response, jsonify
import sqlite3
import requests
#werkzeug error codes custom

app = Flask(__name__)

api_key = "e4be59005046fe7d0c8a37e05bca772e5c72e"
url = "https://www.thepythoncode.com/topic/using-apis-in-python"

# urls = [[1, 'google', 'wwww.google.com'], [1, 'google', 'wwww.google.com'], [1, 'google', 'wwww.google.com']]

def get_db_connection():
    conn = sqlite3.connect('shortURL.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        
        new_url = request.form["url"],

        print(new_url[0])
        
        api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={new_url[0]}"
        
        data = requests.get(api_url).json()["url"]
        if data["status"] == 7:
            # OK, get shortened URL
            shortened_url = data["shortLink"]
            print("Shortened URL:", shortened_url)
            # urls.append(shortened_url)
            conn = get_db_connection()
            conn.execute("INSERT INTO shortURL (URL, shortURL) VALUES (?, ?)", (new_url[0], shortened_url))
            conn.commit()
            conn.close() 
        else:
            print("[!] Error Shortening URL:", data)

        return render_template('home.html', title='POKEMON', urls=urls)

    else:
        return render_template('home.html', title='POKEMON', urls=urls)

@app.route('/urls')
def urls():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM shortURL').fetchall()
    conn.close()
    url_list = []
    for p in posts:
        url_list.append({'id': p['id'], 'URL': p['URL'], 'shortURL':p['shortURL']})
    return jsonify(url_list)


if __name__ == '__main__':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + shortUrl.db
    app.run()

