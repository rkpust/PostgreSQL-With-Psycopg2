import psycopg2 #pip install psycopg2 
import psycopg2.extras
from decouple import config #pip install django-decouple

# Get the database credentials from the .env file
db_name = config('DB_NAME')
db_user = config('DB_USER')
db_password = config('DB_PASSWORD')
db_host = config('DB_HOST')
db_port = config('DB_PORT')

try:
    # Establish the connection
    conn = psycopg2.connect(
        dbname=db_name,
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port
    )

    print(db_name,db_user,db_password,db_host,db_port)
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    query = "SELECT * FROM todos_todo;"
    #query = "INSERT INTO todos_todo (id, content) VALUES(2,'Running');"
    #query = "UPDATE todos_todo SET content ='Updated Running' WHERE id = 2;"
    #query = "DELETE FROM todos_todo WHERE id = 2;"
    cur.execute(query)
    print(cur.fetchall())
except(Exception, psycopg2.DatabaseError) as err:
    print(err)
finally:
    #commit method save all change of DB, specially used in UPDATE & INSERT operation
    conn.commit()
    cur.close()
    conn.close()