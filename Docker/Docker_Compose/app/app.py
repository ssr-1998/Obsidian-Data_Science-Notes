from flask import Flask, request, jsonify
import mysql.connector
import redis
import os
import json
import time

app = Flask(__name__)

# Load environment variables
MYSQL_HOST = os.environ.get('MYSQL_HOST', 'localhost')
MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', '')
MYSQL_DB = os.environ.get('MYSQL_DB', 'flaskdb')
REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')

# Setup Redis
r = redis.Redis(host=REDIS_HOST, port=6379, decode_responses=True)

# Retry DB connection in case DB isn't up yet
def get_db_connection(retries=5, delay=3):
    for i in range(retries):
        try:
            conn = mysql.connector.connect(
                host=MYSQL_HOST,
                user=MYSQL_USER,
                password=MYSQL_PASSWORD,
                database=MYSQL_DB
            )
            return conn
        except mysql.connector.Error as err:
            print(f"DB connection failed: {err}, retrying in {delay}s...")
            time.sleep(delay)
    raise Exception("Unable to connect to MySQL after multiple retries")

# Create the table if it doesn't exist
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100)
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()
    print("✅ MySQL table ensured.")

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    name = data['name']
    email = data['email']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    conn.commit()
    cursor.close()
    conn.close()

    # Invalidate Redis cache
    r.delete('users')

    return jsonify({'message': 'User added successfully'}), 201

@app.route('/users', methods=['GET'])
def get_users():
    cached_users = r.get('users')
    if cached_users:
        return jsonify({'source': 'cache', 'users': json.loads(cached_users)})

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email FROM users")
    users = [{'id': id, 'name': name, 'email': email} for (id, name, email) in cursor.fetchall()]
    cursor.close()
    conn.close()

    r.set('users', json.dumps(users), ex=30)

    return jsonify({'source': 'db', 'users': users})

if __name__ == '__main__':
    print("🔧 Initializing database...")
    init_db()
    app.run(host='0.0.0.0', port=5000)
