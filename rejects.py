from datetime import datetime
import psycopg2
import os

def store_rejects(rejects_dict):
    keys = []
    vals = []

    for key, val in rejects_dict.items():
        keys.append(key)
        vals.append(val)

    keys = ', '.join([str(key) for key in keys])
    vals = ', '.join([str(val) for val in vals])

    timestamp = datetime.now().strftime('%Y-%m-%d')

    keys = keys + ', ' + 'date'
    vals = f"{vals}, '{timestamp}'"

    query = f"INSERT INTO rejects({keys}) VALUES ({vals});"

    conn = psycopg2.connect(f"dbname=mydb \
                        user={os.environ['DB_USER']} \
                        password={os.environ['DB_PASSWORD']}")
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()
