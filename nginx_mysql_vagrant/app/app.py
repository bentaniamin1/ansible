from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def hello():
    try:
        db = mysql.connector.connect(
            host="192.168.33.11",
            user="test",
            password="test_password",
            database="db_test"
        )
        return "Connected to MySQL!"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)