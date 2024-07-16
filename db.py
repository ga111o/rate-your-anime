import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE users
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  username TEXT UNIQUE,
                  hashed_password TEXT,
                  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')

cursor.execute('''CREATE TABLE anime
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT,
                  director TEXT)''')

cursor.execute('''CREATE TABLE episode
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT,
                  anime_id INTEGER,
                  FOREIGN KEY (anime_id) REFERENCES anime(id))''')

cursor.execute('''CREATE TABLE anime_ratings
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  user_id INTEGER,
                  anime_id INTEGER,
                  score INTEGER,
                  FOREIGN KEY (user_id) REFERENCES users(id),
                  FOREIGN KEY (anime_id) REFERENCES anime(id))''')

cursor.execute('''CREATE TABLE episode_ratings
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  user_id INTEGER,
                  episode_id INTEGER,
                  score INTEGER,
                  FOREIGN KEY (user_id) REFERENCES users(id), FOREIGN KEY (episode_id) REFERENCES episode(id))''')

conn.commit()
conn.close()