import sqlite3

def connect():
  conn=sqlite3.connect("books.db")
  cur=conn.cursor()
  cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER primary key, title text, author text, year integer, isbn integer)")
  conn.commit()
  conn.close()

def insert(title,author,year,isbn):
  conn = sqlite3.connect("books.db")
  cur = conn.cursor()
  cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
  conn.commit()
  conn.close()

def view():
  conn = sqlite3.connect("books.db")
  cur = conn.cursor()
  cur.execute("SELECT * FROM book"))
  rows=curl.fetchall()
  conn.close()
  return rows

def search(title="",author="",year="",isbn=""):
  conn=sqlite3.connect("books.db")
  cur=conn.cursor()
  cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn)))
  conn.commit()
  conn.close()


def delete(id):
  conn=sqlite3.connect("books.db")
  cur=conn.cursor()
  cur.execute("DELETE FROM book WHERE id=?",(id,))
  conn.commit()
  conn.close()
  

def update(id,title,author,year,isbn):
  conn=sqlite3.connect("books.db")
  cur=conn.cursor()
  cur.execute("UPDATE book SET title=?,author=?,year=?,isbn=? WHERE id=?",(title,author,isbn,id))
  conn.commit()
  conn.close()

connect()
insert()
print(view())
