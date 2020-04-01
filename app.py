"""
This is my first python application that is being deployed on SAP Cloud Platform in the Cloud Foundry environment
"""
from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Api,Resource, fields
import os

app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)
port = int(os.getenv("PORT", 9009))

class Name(db.Model):
    id = db.Column(db.Integer, nullable=True, primary_key=True)
    text = db.Column(db.String(20), nullable=False)

a_name = api.model('Name',{'name' :fields.String('The name.')})

@api.route('/')
class NameOperation(Resource):
    def get(self):
        texts = list(map(lambda name: name.text,Name.query.all()))
        return texts
    @api.expect(a_name)
    def post(self):
        name = api.payload
        db.session.add(name)
        db.session.commit()
        return {'result':'Name added'}, 201

if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', port=port)