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

a_language = api.model('Language', {'language' : fields.String('The language.')})
class Name(db.Model):
    id = db.Column(db.Integer, nullable=True, primary_key=True)
    text = db.Column(db.String(20), nullable=False)

languages = []
python = {'language':'Python'}
languages.append(python)

@api.route('/language')
class language(Resource):
    def get(self):
        return languages
    
    @api.expect(a_language)
    def post(self):
        languages.append(api.payload)
        return {'result':'Language added'}, 201


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