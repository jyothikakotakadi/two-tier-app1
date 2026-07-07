
from flask import Flask
import mysql.connector
import time

app = Flask(__name__)

def get_connection():
    while True:
        try:
            conn = mysql.connector.connect(
                host="db",
                user="root",
                password="root123",
                database="studentdb"
            )
            return conn
        except:
            print("Waiting for MySQL...")
            time.sleep(5)

@app.route('/')
def home():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return f"Students: {data}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
