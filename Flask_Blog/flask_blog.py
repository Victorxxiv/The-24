from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'auhor': 'Victor Mwendwa',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'August 02, 2024'
    },
    {
        'auhor': 'Ragnar Rock',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'August 03, 2024'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/blog")
def blog():
    return render_template('blog.html')

if __name__ == '__main__':
    app.run(debug=True)