from flask import Blueprint
from flask import Flask,render_template,request,redirect
from Name import Name

index_bp = Blueprint('index_bp', __name__,
    template_folder='templates',)

@index_bp.route('/', methods=['GET',"POST"])
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