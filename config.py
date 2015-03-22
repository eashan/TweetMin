#default config
import os
class BaseConfig(object):
	DEBUG=False
	secret_key="my_precious"
	SQLALCHEMY_DATABASE_URI='postgresql:///tweetmin'
	os.environ['DATABASE_URI']
	#for mysql :'mysql://root:eashanrocks@localhost/posts'
	print SQLALCHEMY_DATABASE_URI
class DevelopmentConfig(BaseConfig):
	DEBUG=True