import psycopg2
import os

conn = None
if "DATABASE_URL" in os.environ:
    DATABASE_URL = os.environ["DATABASE_URL"]
else:
    DATABASE_URL = "host=localhost user=aivant dbname=pythonsqldb"
print("Using database URL:", DATABASE_URL)
try:
    conn = psycopg2.connect(DATABASE_URL)
    print("Connecteed!")
except psycopg2.DatabaseError as e:
    print('I am unable to connect the database: ', e)
cur = conn.cursor()


def get_posts():
    try:
        cur.execute("SELECT * FROM post;")
        ans = cur.fetchone()
        print("Get posts answer: ", ans)
        return ans or "blank"
    except psycopg2.Error as e:
        print("error in getting posts:",e)
        conn.rollback();
        return "blank"


def create_post(title, description):
    try:
        print("Creating post\ntitle: " + title + "\ndescription: " + description)
        cur.execute("INSERT INTO post VALUES ('{0}', '{1}');".format(title, description))
        conn.commit()
        # do nothing
    except psycopg2.Error as e:
        print("Create error", e)
        conn.rollback()

def init_db():
    try:
        print("Initializing db")
        cur.execute("CREATE TABLE post (title text, description text);")
        conn.commit()
    except psycopg2.Error as e:
        print("Init error", e)
        conn.rollback()
    # Do nothing

def drop_db():
    try:
        cur.execute("DROP TABLE post")
        conn.commit()
    except psycopg2.Error as e:
        print("drop error", e)
        conn.rollback()
