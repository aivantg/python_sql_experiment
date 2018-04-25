import psycopg2
import os

conn = None
if "DATABASE_URL" in os.environ:
    DATABASE_URL = os.environ["DATABASE_URL"]
else:
    DATABASE_URL = "host=localhost user=aivant dbname=pythonsqldb"

try:
    conn = psycopg2.connect(DATABASE_URL)
    print("Connecteed!")
except psycopg2.DatabaseError:
    print('I am unable to connect the database: ')
cur = conn.cursor()


def get_posts():
    cur.execute("SELECT * FROM post;")
    ans = cur.fetchone()
    print(ans)
    return ans


def create_post(title, description):
    print("Creating post\ntitle: " + title + "\ndescription: " + description)
    cur.execute("INSERT INTO post VALUES ('{0}', '{1}');".format(title, description))
    conn.commit()
    # do nothing

def init_db():
    print("Initializing db")
    cur.execute("CREATE TABLE post (title text, description text);")
    conn.commit()
    # Do nothing

def drop_db():
    cur.execute("DROP TABLE post")
    conn.commit()
