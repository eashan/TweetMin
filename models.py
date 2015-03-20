from app import db




class blogpost(db.Model):
	__tablename__='posts';
	id=db.Column(db.Integer,primary_key='true')
	title=db.Column(db.String(10000),nullable='false')
	description=db.Column(db.String(100000),nullable='false')

	def __init__(self,title,description):
		self.title=title
		self.description=description
	def __repr__(self):
		return '<title:{}>'.format(self.title)

