import psycopg2 #pip install psycopg2 
import psycopg2.extras


# Get the database credentials
DB_HOST = "localhost"
DB_NAME = "RingDB"
DB_USER = "postgres"
DB_PASS = "12345678"

try:
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    #query = "SELECT * FROM ring_info;"
    #query = "SELECT * FROM ring_info WHERE type = 'new' AND status = 'free';"
    #query = "INSERT INTO ring_info(id, name, type, ring_no, status, created_at, created_by) VALUES (1, 'CTG_TEL_AGG_00001', 'old', 1, 'active', NOW(), '02-2366');"
    #query = "INSERT INTO ring_info(id, name, type, ring_no, status, created_at, created_by) VALUES (15, 'D-E-F-00015', 'is3', 15, 'active', NOW(), '02-2366');"
    #query = "INSERT INTO ring_info(id, name, type, ring_no, status, created_at, created_by) VALUES (25, 'G-H-I-00025', 'new', 25, 'active', NOW(), '02-2366');"
    query = "UPDATE ring_info SET name='RNG_FHL_AGG_00003' WHERE id = 3;"
    #query = "DELETE FROM ring_info WHERE status = 'active';"
    # query = "SELECT id FROM ring_info WHERE name LIKE '%BRG_TEL%';"
    cur.execute(query)
    print(cur.fetchall())
except(Exception, psycopg2.DatabaseError) as err:
    print(err)
finally:
    #commit method save all change of DB, specially used in UPDATE & INSERT operation
    conn.commit()
    cur.close()
    conn.close()