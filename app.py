from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Replace these values with your actual MySQL database credentials
db_config = {
    'host': 'localhost',
    'port': 3308,
    'user': 'root',
    'password': '',
    'database': 'pythonanywhere_db'
}

def fetch_user():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Fetch a user from the database (change the query as per your table structure)
    cursor.execute("SELECT name FROM tbl_users LIMIT 1")
    user = cursor.fetchone()

    cursor.close()
    connection.close()

    return user[0] if user else None

@app.route('/')
def index():
    # Fetch a user from the database
    user_name = fetch_user() or 'Guest'
    return render_template('welcome.html', name=user_name)

if __name__ == '__main__':
    app.run(debug=True)
