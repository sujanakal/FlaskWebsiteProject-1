from flask import Flask, render_template 

app = Flask(__name__)
app.url_map.strict_slashes = False

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