from app import db
from models import blogpost


#create the database and db tables
db.create_all()

#insert
db.session.add(blogpost("Hello there","We are chattty"))
db.session.add(blogpost("How are you doing?","I am super cool"))

#commit changes

db.session.commit()