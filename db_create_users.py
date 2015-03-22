from app import db
from models import user

db.session.add(user('eashan','eashankadam@gmail.com','eashantodu'))
db.session.add(user('anish','shahanish07@gmail.com','anishshah'))

db.session.commit()