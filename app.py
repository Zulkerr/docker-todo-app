from flask import Flask, render_template, request, redirect, url_for, jsonify
import psycopg2
import os
from datetime import datetime

app = Flask(__name__)

# Datenbank-Verbindung
def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST', 'postgres'),
        database=os.getenv('DB_NAME', 'todoapp'),
        user=os.getenv('DB_USER', 'postgres'),
        password=os.getenv('DB_PASSWORD', 'postgres')
    )
    return conn

# Startseite - alle To-Dos anzeigen
@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM todos ORDER BY created_at DESC')
    todos = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', todos=todos)

# Neues To-Do hinzufügen
@app.route('/add', methods=['POST'])
def add_todo():
    title = request.form['title']
    description = request.form['description']
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO todos (title, description) VALUES (%s, %s)',
                (title, description))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))

# To-Do als erledigt markieren
@app.route('/complete/<int:todo_id>')
def complete_todo(todo_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('UPDATE todos SET completed = TRUE WHERE id = %s', (todo_id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))

# To-Do löschen
@app.route('/delete/<int:todo_id>')
def delete_todo(todo_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM todos WHERE id = %s', (todo_id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 
