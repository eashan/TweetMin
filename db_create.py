from app import db
from models import blogpost


#create the database and db tables
db.create_all()

#demo insert statements
db.session.add(blogpost("Hello there","We are chattty"))
db.session.add(blogpost("How are you doing?","I am super cool"))
db.session.add(blogpost("Postgress","We just setup a local postgres instance"))

#commit changes

db.session.commit()