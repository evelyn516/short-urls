from flask import Flask, render_template, redirect, url_for, request, Response
import sqlite3
import requests
#werkzeug error codes custom

app = Flask(__name__)

api_key = "e4be59005046fe7d0c8a37e05bca772e5c72e"

def get_db_connection():
    conn = sqlite3.connect('URL.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        
        new_url = request.form["url"],

        print(new_url)

        conn = get_db_connection()
        new_row = conn.execute("INSERT INTO pokemon (name, type, level) VALUES (?, ?, ?)", (new_name[0], new_type[0], new_level,))
        conn.commit()
        conn.close()

        return render_template('home.html', title='POKEMON', pokelist=show_pokedex())    
    else:
        return render_template('home.html', title='POKEMON', pokelist=show_pokedex())

if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'your secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['TRAP_HTTP_EXCEPTIONS']=True
    app.run(debug=True)

