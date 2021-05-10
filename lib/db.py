import psycopg2


class Database:


	def __init__(self, dbname='postgresql', host='127.0.0.1', password='password', port=5432, user='admin'):
		self.dbname = dbname
		self.host = host
		self.password = password
		self.port = port
		self.user = user


	def users_list(self, fullname=''):
		self.conn = psycopg2.connect(dbname=self.dbname, host=self.host, password=self.password, port=self.port, user=self.user)
		self.cur = self.conn.cursor()
		q = "SELECT * FROM users WHERE fullname ILIKE '%{}%';".format(fullname)
		self.cur.execute(q)
		l = self.cur.fetchall()
		self.cur.close()
		self.conn.close()
		return l


	def users_add(self, fullname='', occupation=''):
		self.conn = psycopg2.connect(dbname=self.dbname, host=self.host, password=self.password, port=self.port, user=self.user)
		self.cur = self.conn.cursor()
		self.cur.execute("INSERT INTO users (fullname,occupation) VALUES (%s,%s);", (fullname, occupation))
		self.conn.commit()
		self.cur.close()
		self.conn.close()


	def users_remove(self, fullname=''):
		self.conn = psycopg2.connect(dbname=self.dbname, host=self.host, password=self.password, port=self.port, user=self.user)
		self.cur = self.conn.cursor()
		q = "DELETE FROM users WHERE fullname ILIKE '%{}%';".format(fullname)
		self.cur.execute(q)
		self.conn.commit()
		self.cur.close()
		self.conn.close()

