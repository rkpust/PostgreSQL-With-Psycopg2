DB_HOST = "localhost"
DB_NAME = "ecommerce"
DB_USER = "admin"
DB_PASS = "ecommerce"
 
import psycopg2 #pip install psycopg2 
import psycopg2.extras
 
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
 
#cur.execute("INSERT INTO accounts (user_id, username, password, email, created_on, last_login) VALUES(%s,%s,%s,%s,%s,%s)", ("4","user2","pass2","user4@gmail.com","2021-04-01","2021-01-01"))
 
cur.execute("SELECT * FROM cars;")
print(cur.fetchall())
 
conn.commit()
cur.close()
conn.close()