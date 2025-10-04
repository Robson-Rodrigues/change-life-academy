from flask import Flask, render_template, request, redirect, url_for, session, flash
import json
import os

app = Flask(__name__)
app.secret_key = 'change_life_academy_secret_key_2024'

# Carregar usuários do arquivo JSON
def load_users():
    try:
        with open('users.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_users(users):
    with open('users.json', 'w', encoding='utf-8') as f:
        json.dump(users, f, ensure_ascii=False, indent=2)

@app.route('/')
def index():
    if 'user' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    show_modal = False
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Aceitar qualquer usuário, mas senha deve ser 123456
        if username.strip() and password == '123456':
            session['user'] = {
                'username': username,
                'name': username.title(),  # Capitalizar o nome
                'role': 'user'  # Role padrão
            }
            return redirect(url_for('dashboard'))
        elif username.strip() and password.strip():
            show_modal = True
    
    return render_template('login.html', show_modal=show_modal)

@app.route('/chatbot')
def chatbot():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    return render_template('chatbot.html', user=session['user'])

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    user = session['user']
    return render_template('dashboard.html', user=user)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
