from flask import Flask, render_template 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///caprastellar.db'

db = SQLAlchemy(app)

class Blogpost(db.Model):
    #Database columns
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100))
    posted_on = db.Column(db.String(20))
    comments = db.Column(db.Integer)
    content = db.Column(db.String(300))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')    

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/work')
def work():
    return render_template('work.html')

if __name__ == '__main__':
    app.run(debug = True)