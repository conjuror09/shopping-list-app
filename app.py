from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# In-memory shopping list (for simplicity)
shopping_list = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        item = request.form['item']
        shopping_list.append(item)
        return redirect(url_for('index'))
    return render_template('index.html', items=shopping_list)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')