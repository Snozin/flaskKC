from flask import render_template
from app import app


@app.route('/<name>')
def index(name):
  # return 'Enigma funcionará aquí!'
  return render_template("index.html", nombre=name)