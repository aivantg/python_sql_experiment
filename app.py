from flask import Flask, render_template, request, redirect, json
import generator
import database
app = Flask(__name__)

@app.route("/")
def index():
    generator.generate_index()
    return render_template('index.html')

@app.route("/new")
def new():
    return "new"

@app.route("/init")
def init():
    database.init_db()
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

@app.route('/create', methods=['POST'])
def create():
    database.create_post(request.form['title'], request.form['description'])
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}


if __name__ == "__main__":
	app.run()
