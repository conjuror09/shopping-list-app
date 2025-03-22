import os
import logging
import sqlite3
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for

# Load environment variables from .env file (if it exists)
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Get configuration from environment variables
SECRET_KEY = os.environ.get('SECRET_KEY', 'your_default_secret_key')
DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///:memory:')
PORT = int(os.environ.get('PORT', 5000))
FLASK_DEBUG = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'

app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = SECRET_KEY
app.config['DATABASE'] = os.path.join(app.root_path, 'shopping_list.db')


def get_db_connection():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


# In-memory shopping list (for simplicity)
# shopping_list = [] #Removed
# Code will break.
@app.route('/', methods=['GET', 'POST'])
def index():
    create_table()
    conn = get_db_connection()
    if request.method == 'POST':
        item = request.form['item']
        cursor = conn.cursor()
        cursor.execute("INSERT INTO items (item) VALUES (?)", (item,))
        conn.commit()
        logger.info(f"Added item: {item}")
        return redirect(url_for('index'))
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    conn.close()
    return render_template('index.html', items=items)


@app.route('/health')
def health_check():
    return "OK", 200


if __name__ == '__main__':
    # Use a production WSGI server (e.g., Gunicorn) instead of app.run()
    # To run with gunicorn, run `gunicorn --bind 0.0.0.0:$PORT app:app`
    app.run(debug=FLASK_DEBUG, host='0.0.0.0', port=PORT)
