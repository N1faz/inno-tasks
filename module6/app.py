#!/usr/bin/env python3
import os
import redis
from flask import Flask
import psycopg2

app = Flask(__name__)

DATABASE_URL = os.getenv("DATABASE_URL")
conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()

REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379")
redis_client = redis.Redis.from_url(REDIS_URL)

cur.execute("""
    CREATE TABLE IF NOT EXISTS visits (
        id SERIAL PRIMARY KEY,
        visit_time TIMESTAMP DEFAULT NOW()
    );
""")
conn.commit()

@app.route('/')
def hello():
    count = redis_client.incr("visits_count")

    cur.execute("INSERT INTO visits DEFAULT VALUES;")
    conn.commit()

    return f" Привет! Ты {count} посетитель!"

@app.route('/health')
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
