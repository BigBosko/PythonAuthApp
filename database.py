import sqlite3 as sql
import bcrypt

DB_FILE ="user_auth.db"

def create_user_table():
    con=sql.connect(DB_FILE)
    cur = con.cursor()
    #podatkovni tip text in varchar(n) sta v sqlite enaka (n) ni meja
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password_hash BLOB NOT NULL
        )
    """)
    con.commit()
    con.close()

def hashed_pass(password):
    pass_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pass_bytes, salt)

def add_user(username, password):
    con=sql.connect(DB_FILE)
    cur = con.cursor()
    pass_hash = hashed_pass(password)
    cur.execute("INSERT INTO users(username, password_hash) VALUES(?,?)", (username, pass_hash))
    con.commit()
    con.close()
    

def is_login_correct(username, password):
    con=sql.connect(DB_FILE)
    cur = con.cursor()
    cur.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
    row = cur.fetchone()
    con.close()
    if row:
        password_hash_DB = row[0]
        return bcrypt.checkpw(password.encode('utf-8'), password_hash_DB)
    return False

def is_username_unique(username):
    con=sql.connect(DB_FILE)
    cur = con.cursor()
    cur.execute("SELECT 1 FROM users WHERE username = ?", (username,)) #pogleda če najde točno takšen username
    result = cur.fetchone()
    con.close()
    return result is None

create_user_table()