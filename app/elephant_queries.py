# app/elephant_queries.py

import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()   # loads contents of the .env file into the script's enviornment

DB_NAME = os.getenv("DB_NAME")					
DB_USER = os.getenv("DB_USER")			
DB_PASSWORD = os.getenv("DB_PASSWORD")		
DB_HOST = os.getenv("DB_HOST")			

### Connect to ElephantSQL-hosted PostgreSQL
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print(type(conn))

### A "cursor", a structure to iterate over db records to perform queries
cur = conn.cursor()
print(type(cur))

### An example query
query = 'SELECT count(name) from test_table;'

### Note - nothing happened yet! We need to actually *fetch* from the cursor

cur.execute(query)
results = cur.fetchone()
print(type(results))
print(results)
