import os
import logging
from dotenv import load_dotenv  # Import load_dotenv
from flask import Flask, render_template, request, redirect, url_for

# Load environment variables from .env file (if it exists)
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Get configuration from environment variables
SECRET_KEY = os.environ.get('SECRET_KEY', 'your_default_secret_key')
DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///:memory:')
PORT = int(os.environ.get('PORT', 5000))
FLASK_DEBUG = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'

app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = SECRET_KEY

# In-memory shopping list (for simplicity)
shopping_list = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        item = request.form['item']
        shopping_list.append(item)
        logger.info(f"Added item: {item}")
        return redirect(url_for('index'))
    return render_template('index.html', items=shopping_list)

@app.route('/health')
def health_check():
    return "OK", 200

if __name__ == '__main__':
    # Use a production WSGI server (e.g., Gunicorn) instead of app.run()
    # To run with gunicorn, run `gunicorn --bind 0.0.0.0:$PORT app:app`
    app.run(debug=FLASK_DEBUG, host='0.0.0.0', port=PORT)