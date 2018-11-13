from app import app
from flask import render_template
from app import models
from bs4 import BeautifulSoup



@app.route('/')
@app.route('/index')
def index():
    blogs = models.Blog.query.all()
    blogs1 = list()
    for bl in blogs:
        soup = BeautifulSoup(bl.content, "html.parser")
        bf = soup.get_text()[0:10] + '...'
        blogs1.append({"title": bl.title, "bf": bf, "id": bl.id})
    return render_template("index.html", blogs=blogs1)

@app.route('/about/<int:id>')
def about(id):
    about = models.Blog.query.filter_by(id=id).first()
    return render_template("about.html", about=about)
