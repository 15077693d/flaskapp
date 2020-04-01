"""
This is my first python application that is being deployed on SAP Cloud Platform in the Cloud Foundry environment
"""
from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
db = SQLAlchemy(app)
port = int(os.getenv("PORT", 9009))

class Name(db.Model):
    id = db.Column(db.Integer, nullable=True, primary_key=True)
    text = db.Column(db.String(20), nullable=False)
    
@app.route('/', methods=['GET',"POST"])
def index():
    if request.method =="POST":
        name = Name(text = request.form['text'])
        try:
            db.session.add(name)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return e
    else:
        texts = list(map(lambda name: name.text,Name.query.all()))
        return render_template('index.html', texts = texts)

if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', port=port)