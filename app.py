import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///patients.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def home():
    return "Welcome to the Chronic Care Management System!"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use port from environment or default to 5000
    app.run(host='0.0.0.0', port=port)
