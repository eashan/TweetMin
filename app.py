# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request, session, flash,g
from functools import wraps
#import sqlite3
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
# create the application object
app = Flask(__name__)

# config
app.secret_key = 'my precious'
#app.database='chattty.db'
bcrypt=Bcrypt(app)
#config

app.config.from_object('config.DevelopmentConfig')

#create sqlalchemy object
db=SQLAlchemy(app)

#import database
from models import *
# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

# use decorators to link the function to a url
@app.route('/',methods=['GET','POST'])
@login_required
def home():
    error=None
    if request.method=='POST':
        user1=user.query.filter_by(email=session['loginemail']).first()
        db.session.add(blogpost(request.form['tweet'],user1.id))
        db.session.commit()
        return redirect(url_for('home'))
    #g.db=connect_db()
    #cur=g.db.execute("select * from posts")
    #posts=[dict(title=row[0],description=row[1]) for row in cur.fetchall()]
    #g.db.close()
    posts=db.session.query(blogpost).all()
    return render_template('index.html',posts=posts)  # render a template
    # return "Hello, World!"  # return a string

@app.route('/signup',methods=['GET','POST'])
def signup():
    error=None
    if request.method=='POST':
        repemail=user.query.filter_by(email=request.form['email']).first()
        if(repemail is None):
            if request.form['uname']=='':
                error='Please enter Username'
                return render_template('signup.html',error=error) 
            elif request.form['passw']=='':
                error="Please enter Password"
                return render_template('signup.html',error=error) 
            else:
                db.session.add(user(request.form['uname'],request.form['email'],request.form['passw']))
                db.session.commit()
                session['logged_in'] = True
                session['loginemail']=request.form['email']
                session['loginuser']=request.form['uname']
                flash('You were logged in.')
                return redirect(url_for('home'))

        else:
            error='already registered'
            flash('Already Registered')
    return render_template('signup.html') 
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user1=user.query.filter_by(email=request.form['email']).first()
        if(user1 is None):
            flash('You need to signup.')
            return redirect(url_for('signup'))
        else:
            if bcrypt.check_password_hash(user1.password,request.form['password']):
                session['logged_in'] = True
                session['loginemail']=user1.email
                session['loginuser']=user1.name
                flash('You were logged in.')
                return redirect(url_for('home'))

            else:
                 error = 'Invalid Credentials. Please try again.'       
    return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were logged out.')
    return redirect(url_for('welcome'))


#def connect_db():
#   return sqlite3.connect(app.database)
# start the server with the 'run()' method
if __name__ == '__main__':
    app.run()