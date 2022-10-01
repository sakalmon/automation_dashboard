import psycopg2
import os

def store_one():
    conn = psycopg2.connect(f"dbname=mydb \
                            user={os.environ['DB_USER']} \
                            password={os.environ['DB_PASSWORD']}")
    cur = conn.cursor()
    cur.execute("INSERT INTO rejects (optic_press) VALUES (10)")
    conn.commit()
    cur.close()
    conn.close()

store_one()