from flask import Flask, render_template
from forms import UserForm



app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'


@app.route("/", methods=['GET','POST'])
@app.route("/login", methods=['GET','POST'])
def login():
    form = UserForm()
    return render_template('login.html', form=form)



@app.route('/movies')
def show_movies():
    movies = [
        {"title": "Jurassic Park", "year": 1993, "director": "Steven Spielberg"},
        {"title": "The Lost World: Jurassic Park", "year": 1997,
         "director": "Steven Spielberg"}
    ]
    return render_template('movies.html', movies=movies)




