from flask import Flask, render_template
from forms import UserRegistration



app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'

@app.route('/')
@app.route('/login',methods=['GET', 'POST'])
def login_page():
    form = UserRegistration()


    return render_template('login.html', form=form)