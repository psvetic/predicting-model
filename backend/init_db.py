import os
import psycopg2
from datetime import datetime

'''from psycopg2 import sql

query = sql.SQL("CREATE USER {username} WITH PASSWORD {password}").format(
    username=sql.Identifier('abcdefgh'),
    password=sql.Placeholder()
)
cur.execute(query, ('0h/9warrAttrgd8EF0gkvQ==',))'''

conn = psycopg2.connect("postgresql://postgres:password@localhost:3001/postgres")

cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS searchresults;')
cur.execute('CREATE TABLE searchresults (id serial PRIMARY KEY,'
                                 'file_name varchar (100) NOT NULL,'
                                 'response_timestamp timestamp NOT NULL,'
                                 'barcode integer NOT NULL,'
                                 'response_text text,'
                                 'probability decimal,'
                                 'request_duration decimal);'
                                 )

conn.commit()

'''cur.execute("SELECT * FROM searchresults")

records = cur.fetchall()

print(records)'''

cur.close()
conn.close()