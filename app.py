"""
This is my first python application that is being deployed on SAP Cloud Platform in the Cloud Foundry environment
"""
from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

import os

app = Flask(__name__)
from IndexController import index_bp
app.register_blueprint(index_bp)
db = SQLAlchemy(app)
port = int(os.getenv("PORT", 9009))

if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', port=port)