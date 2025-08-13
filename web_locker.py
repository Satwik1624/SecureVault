from flask import Flask, render_template, request, redirect, url_for, session, flash, send_file
from digital_locker import DigitalLocker
import os
import base64
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'digital_locker_secret_key'
locker = DigitalLocker()

@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        pin = request.form['pin']
        success, message = locker.register_user(username, pin)
        if success:
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('home'))
        else:
            flash(message, 'error')
    return render_template('register.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    pin = request.form['pin']
    if locker.login(username, pin):
        session['username'] = username
        return redirect(url_for('dashboard'))
    else:
        flash('Invalid credentials', 'error')
    return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('home'))
    
    locker.current_user = session['username']
    files = locker.list_files()
    return render_template('dashboard.html', files=files, username=session['username'])

@app.route('/store', methods=['POST'])
def store_file():
    if 'username' not in session:
        return redirect(url_for('home'))
    
    locker.current_user = session['username']
    
    if 'file' in request.files and request.files['file'].filename:
        file = request.files['file']
        filename = secure_filename(file.filename)
        content = base64.b64encode(file.read()).decode('utf-8')
        success, message = locker.store_file(filename, content)
    else:
        filename = request.form['filename']
        content = request.form['content']
        success, message = locker.store_file(filename, content)
    
    flash(message, 'success' if success else 'error')
    return redirect(url_for('dashboard'))

@app.route('/view/<filename>')
def view_file(filename):
    if 'username' not in session:
        return redirect(url_for('home'))
    
    locker.current_user = session['username']
    success, content = locker.retrieve_file(filename)
    if success:
        try:
            decoded_content = base64.b64decode(content).decode('utf-8')
            is_text = True
        except:
            decoded_content = content
            is_text = True
        return render_template('view_file.html', filename=filename, content=decoded_content, is_text=is_text)
    else:
        flash(content, 'error')
        return redirect(url_for('dashboard'))

@app.route('/delete/<filename>')
def delete_file(filename):
    if 'username' not in session:
        return redirect(url_for('home'))
    
    locker.current_user = session['username']
    success, message = locker.delete_file(filename)
    flash(message, 'success' if success else 'error')
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)