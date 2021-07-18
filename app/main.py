from fastapi import FastAPI, Request
import psycopg2
import os

app = FastAPI()

def connect_to_database():
    conn = psycopg2.connect(
	   database="ips", 
	    user=os.getenv('postgres_username'), 
	    password=os.getenv('postgres_password'), 
	    host=os.getenv('postgres_url'), 
	    port= '5432'
	)
    cursor = conn.cursor()
    return conn,cursor

conn,cursor = connect_to_database()
cursor.execute("create table IF NOT EXISTS ips (ip varchar)")
conn.commit()

@app.get('/')
def say_hello(n: int=None ):
    if n is None:
    	return "Halan ROCKS"
    else:
        return n*n


@app.get('/ip')
def menna(request: Request):
   client_host = request.client.host
   conn,cursor = connect_to_database()
   query = "insert into ips (ip) values ('{}')".format(client_host)
   cursor.execute(query)
   conn.commit()
   return client_host


@app.get('/allips')
def get_allips():   
   conn,cursor = connect_to_database()
   query = "select * from ips"
   cursor.execute(query)
   data = cursor.fetchall()
   return data
