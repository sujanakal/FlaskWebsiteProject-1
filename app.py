from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy 
import utils
import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///caprastellar.db'

db = SQLAlchemy(app)

class Blogpost(db.Model):
    #Database columns
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50))
    posted_on = db.Column(db.DateTime)
    comments = db.Column(db.Integer)
    content = db.Column(db.Text)

@app.route('/')
def index():
    return render_template('index.html', blog_posts = utils.getBlogPosts())

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

@app.route('/blogPost')
def addBlogPost():
    return render_template('blogpost.html')

@app.route('/addPost', methods=['POST'])
def addblogpost():
    title = request.form['title']
    content = request.form['content']

    # post = Blogpost(title=title, posted_on="Oct 23rd", comments=24, content=content )

    # return render_template('addblogpost.html')
    return '<h1>Title: {} Posted on: Oct 24th Comments: 21 Content: {}'.format(title,content)

if __name__ == '__main__':
    app.run(debug = True)