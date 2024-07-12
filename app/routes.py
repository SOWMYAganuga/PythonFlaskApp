from flask import render_template # type: ignore
from app import app

@app.route('/')
def index():
    return render_template('index.html', message="Hello, World!")
