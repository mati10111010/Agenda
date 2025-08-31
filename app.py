# app.py en la rama 'diseño'
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create')
def create_task():
    return render_template('create_task.html')
