import sqlite3

with sqlite3.connect("chattty.db") as connection:
	c=connection.cursor()
	c.execute("""create table posts(title TEXT, description TEXT)""")
	c.execute("""insert into posts values ("Eashan","I am so awesome ,I totally rock")""")
